import pytest
from playwright.sync_api import Page, expect


@pytest.mark.regression
def test_lead_conversion_blocked_below_revenue_threshold(page: Page):
    """TC-03: Verify boundary validation when Annual Revenue equals threshold."""
    page.goto("https://demo-crm.example.com/leads/lead-1042")

    page.get_by_role("button", name="Convert Lead").click()
    dialog = page.get_by_role("dialog", name="Convert Lead")
    expect(dialog).to_be_visible()

    dialog.get_by_role("button", name="Confirm Conversion").click()

    error_banner = dialog.get_by_role("alert")
    expect(error_banner).to_contain_text("Annual Revenue must exceed $10,000")
    expect(page).to_have_url("https://demo-crm.example.com/leads/lead-1042")


@pytest.mark.smoke
def test_lead_conversion_succeeds_and_maps_opportunity(page: Page):
    """TC-01: Verify valid lead conversion and downstream Opportunity state."""
    page.goto("https://demo-crm.example.com/leads/lead-1099")

    page.get_by_role("button", name="Convert Lead").click()
    dialog = page.get_by_role("dialog", name="Convert Lead")
    dialog.get_by_role("button", name="Confirm Conversion").click()

    expect(page.get_by_text("Lead successfully converted")).to_be_visible()
    expect(page.get_by_test_id("opportunity-stage")).to_have_text("Prospecting")
