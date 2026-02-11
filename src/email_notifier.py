"""Sends daily email reports via Resend."""

import logging
from datetime import datetime
from typing import Any

import resend

import config
from vault_reader import (
    read_portfolio_positions,
    read_account_status,
    read_previous_agent_output,
)

logger = logging.getLogger(__name__)

resend.api_key = config.RESEND_API_KEY
FROM_EMAIL = "Stock Trading Bot <noreply@uxwritinghub.com>"
TO_EMAIL = config.NOTIFICATION_EMAIL


def send_email(subject: str, html_body: str) -> bool:
    """Send an email via Resend."""
    if not config.RESEND_API_KEY:
        logger.warning("RESEND_API_KEY not set — skipping email")
        return False
    try:
        params = {
            "from": FROM_EMAIL,
            "to": [TO_EMAIL],
            "subject": subject,
            "html": html_body,
        }
        resp = resend.Emails.send(params)
        logger.info(f"Email sent: {subject} (id: {resp.get('id', 'unknown')})")
        return True
    except Exception as e:
        logger.error(f"Email send failed: {e}")
        return False


def send_morning_report(date_str: str, scan_result: dict[str, Any]) -> bool:
    """Send morning scan summary."""
    status = scan_result.get("status", "unknown")
    agent1 = read_previous_agent_output(date_str, 1)
    account = read_account_status()

    # Build a concise summary
    if status == "stand_down":
        headline = "STAND DOWN — No trading today"
        color = "#f59e0b"
    elif status == "approved":
        trades = scan_result.get("trades", [])
        trade_list = "<br>".join(
            f"• {t['symbol']} {t['side'].upper()} {t['qty']} shares "
            f"(stop: ${t['stop_loss']}, target: ${t['take_profit']})"
            for t in trades
        )
        headline = f"TRADE APPROVED — {len(trades)} trade(s) ready"
        color = "#22c55e"
    elif status == "pass":
        headline = "NO TRADE — Setups scored too low"
        color = "#6b7280"
    elif status == "no_setups":
        headline = "NO SETUPS — No technical patterns found"
        color = "#6b7280"
    elif status == "rejected":
        headline = "REJECTED — Gatekeeper blocked the trade"
        color = "#ef4444"
    else:
        headline = f"Status: {status}"
        color = "#6b7280"

    # Trim agent1 output for email
    brief = agent1[:1500] if agent1 else "No investment brief generated."

    html = f"""
    <div style="font-family: -apple-system, sans-serif; max-width: 600px; margin: 0 auto;">
        <div style="background: {color}; color: white; padding: 16px 24px; border-radius: 8px 8px 0 0;">
            <h2 style="margin: 0;">📊 Morning Scan — {date_str}</h2>
            <p style="margin: 4px 0 0; font-size: 18px; font-weight: bold;">{headline}</p>
        </div>
        <div style="background: #f9fafb; padding: 24px; border: 1px solid #e5e7eb;">
            <h3>Account</h3>
            <pre style="background: white; padding: 12px; border-radius: 4px; font-size: 13px;">{account[:500]}</pre>
            <h3>Investment Brief Summary</h3>
            <pre style="background: white; padding: 12px; border-radius: 4px; font-size: 12px; white-space: pre-wrap;">{brief}</pre>
            {f'<h3>Approved Trades</h3><p style="font-size: 15px;">{trade_list}</p>' if status == "approved" else ''}
        </div>
        <div style="background: #374151; color: #9ca3af; padding: 12px 24px; border-radius: 0 0 8px 8px; font-size: 12px;">
            Stock Trading Bot • Paper Trading • Automated Report
        </div>
    </div>
    """

    return send_email(f"📊 {headline} — {date_str}", html)


def send_trade_executed_alert(
    date_str: str, trade_results: list[dict[str, Any]]
) -> bool:
    """Send alert when trades are executed."""
    successful = [r for r in trade_results if r.get("success")]
    failed = [r for r in trade_results if not r.get("success")]

    rows = ""
    for t in successful:
        rows += (
            f"<tr><td style='padding:8px;border-bottom:1px solid #eee;'>{t['symbol']}</td>"
            f"<td style='padding:8px;border-bottom:1px solid #eee;'>{t['side'].upper()}</td>"
            f"<td style='padding:8px;border-bottom:1px solid #eee;'>{t['qty']}</td>"
            f"<td style='padding:8px;border-bottom:1px solid #eee;'>${t['stop_loss']}</td>"
            f"<td style='padding:8px;border-bottom:1px solid #eee;'>${t['take_profit']}</td></tr>"
        )

    html = f"""
    <div style="font-family: -apple-system, sans-serif; max-width: 600px; margin: 0 auto;">
        <div style="background: #22c55e; color: white; padding: 16px 24px; border-radius: 8px 8px 0 0;">
            <h2 style="margin: 0;">🚀 Trade Executed — {date_str}</h2>
            <p style="margin: 4px 0 0;">{len(successful)} order(s) placed{f', {len(failed)} failed' if failed else ''}</p>
        </div>
        <div style="background: #f9fafb; padding: 24px; border: 1px solid #e5e7eb;">
            <table style="width:100%; border-collapse:collapse;">
                <tr style="background:#e5e7eb;">
                    <th style="padding:8px;text-align:left;">Symbol</th>
                    <th style="padding:8px;text-align:left;">Side</th>
                    <th style="padding:8px;text-align:left;">Qty</th>
                    <th style="padding:8px;text-align:left;">Stop</th>
                    <th style="padding:8px;text-align:left;">Target</th>
                </tr>
                {rows}
            </table>
        </div>
        <div style="background: #374151; color: #9ca3af; padding: 12px 24px; border-radius: 0 0 8px 8px; font-size: 12px;">
            Stock Trading Bot • Paper Trading • Automated Report
        </div>
    </div>
    """

    return send_email(f"🚀 {len(successful)} Trade(s) Executed — {date_str}", html)


def send_end_of_day_report(date_str: str) -> bool:
    """Send end-of-day summary with positions and P&L."""
    account = read_account_status()
    positions = read_portfolio_positions()

    html = f"""
    <div style="font-family: -apple-system, sans-serif; max-width: 600px; margin: 0 auto;">
        <div style="background: #3b82f6; color: white; padding: 16px 24px; border-radius: 8px 8px 0 0;">
            <h2 style="margin: 0;">📈 End of Day Report — {date_str}</h2>
        </div>
        <div style="background: #f9fafb; padding: 24px; border: 1px solid #e5e7eb;">
            <h3>Account Status</h3>
            <pre style="background: white; padding: 12px; border-radius: 4px; font-size: 13px;">{account[:800]}</pre>
            <h3>Open Positions</h3>
            <pre style="background: white; padding: 12px; border-radius: 4px; font-size: 13px;">{positions[:800]}</pre>
        </div>
        <div style="background: #374151; color: #9ca3af; padding: 12px 24px; border-radius: 0 0 8px 8px; font-size: 12px;">
            Stock Trading Bot • Paper Trading • Automated Report
        </div>
    </div>
    """

    return send_email(f"📈 End of Day Report — {date_str}", html)


def send_rising_stars_report(date_str: str, results: list[dict]) -> bool:
    """Send rising stars discovery report."""
    if not results:
        return False

    rows = ""
    for r in results:
        signals = ", ".join(r.get("signals", [])[:3])
        rows += (
            f"<tr><td style='padding:8px;border-bottom:1px solid #eee;font-weight:bold;'>{r['ticker']}</td>"
            f"<td style='padding:8px;border-bottom:1px solid #eee;'>{r['score']}/7</td>"
            f"<td style='padding:8px;border-bottom:1px solid #eee;'>${r['price']}</td>"
            f"<td style='padding:8px;border-bottom:1px solid #eee;'>{r['month_change']:+.1f}%</td>"
            f"<td style='padding:8px;border-bottom:1px solid #eee;font-size:12px;'>{signals}</td></tr>"
        )

    html = f"""
    <div style="font-family: -apple-system, sans-serif; max-width: 600px; margin: 0 auto;">
        <div style="background: #8b5cf6; color: white; padding: 16px 24px; border-radius: 8px 8px 0 0;">
            <h2 style="margin: 0;">⭐ Rising Stars Found — {date_str}</h2>
            <p style="margin: 4px 0 0;">{len(results)} new stocks showing breakout potential</p>
        </div>
        <div style="background: #f9fafb; padding: 24px; border: 1px solid #e5e7eb;">
            <table style="width:100%; border-collapse:collapse;">
                <tr style="background:#e5e7eb;">
                    <th style="padding:8px;text-align:left;">Ticker</th>
                    <th style="padding:8px;text-align:left;">Score</th>
                    <th style="padding:8px;text-align:left;">Price</th>
                    <th style="padding:8px;text-align:left;">Month</th>
                    <th style="padding:8px;text-align:left;">Signals</th>
                </tr>
                {rows}
            </table>
        </div>
        <div style="background: #374151; color: #9ca3af; padding: 12px 24px; border-radius: 0 0 8px 8px; font-size: 12px;">
            Stock Trading Bot • Paper Trading • Automated Report
        </div>
    </div>
    """

    return send_email(f"⭐ {len(results)} Rising Stars Found — {date_str}", html)
