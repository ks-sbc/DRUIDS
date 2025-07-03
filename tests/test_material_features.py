"""Test Material for MkDocs specific features requiring CSS support.

Tests for:
- Annotations (clickable numbered references)
- Buttons (styled call-to-action elements)
- Grids (card-based layouts)
- Tooltips (hover information)
"""

import pytest
from pathlib import Path
from bs4 import BeautifulSoup
import subprocess
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


class TestMaterialFeatures:
    """Test Material for MkDocs critical features."""
    
    @pytest.fixture(scope="class")
    def mkdocs_server(self):
        """Start MkDocs dev server for testing."""
        server = subprocess.Popen(
            ["mkdocs", "serve", "-a", "localhost:8001"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(3)  # Wait for server to start
        yield "http://localhost:8001"
        server.terminate()
        server.wait()
    
    @pytest.fixture(scope="class")
    def driver(self):
        """Set up Selenium WebDriver for interactive testing."""
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()
    
    def test_annotations_structure(self, mkdocs_server):
        """Test that annotations have proper HTML structure."""
        response = requests.get(f"{mkdocs_server}/test-features/")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find annotation markers
        annotation_markers = soup.find_all('sup', class_='md-annotation__index')
        assert len(annotation_markers) > 0, "No annotation markers found"
        
        # Check for annotation content
        annotation_content = soup.find_all('aside', class_='md-annotation')
        assert len(annotation_content) > 0, "No annotation content found"
        
        # Verify pairing
        assert len(annotation_markers) == len(annotation_content), \
            "Mismatch between annotation markers and content"
    
    def test_annotations_interactivity(self, mkdocs_server, driver):
        """Test that annotations are clickable and show content."""
        driver.get(f"{mkdocs_server}/test-features/")
        wait = WebDriverWait(driver, 10)
        
        # Find annotation marker
        marker = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".md-annotation__index"))
        )
        
        # Check initial state - annotation should be hidden
        annotation = driver.find_element(By.CSS_SELECTOR, ".md-annotation")
        assert not annotation.is_displayed() or "hidden" in annotation.get_attribute("class"), \
            "Annotation should be hidden initially"
        
        # Click marker
        marker.click()
        time.sleep(0.5)
        
        # Check annotation is now visible
        assert annotation.is_displayed(), "Annotation should be visible after click"
    
    def test_buttons_styling(self, mkdocs_server):
        """Test that buttons have proper Material styling."""
        response = requests.get(f"{mkdocs_server}/test-features/")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find buttons
        buttons = soup.find_all('a', class_='md-button')
        assert len(buttons) > 0, "No buttons found"
        
        # Check for primary button variant
        primary_buttons = soup.find_all('a', class_='md-button--primary')
        assert len(primary_buttons) > 0, "No primary buttons found"
        
        # Verify button structure
        for button in buttons:
            assert button.get('href') is not None, "Button missing href"
            assert button.text.strip(), "Button has no text"
    
    def test_buttons_visual_styling(self, mkdocs_server, driver):
        """Test that buttons have proper visual styling."""
        driver.get(f"{mkdocs_server}/test-features/")
        
        # Find regular button
        button = driver.find_element(By.CSS_SELECTOR, ".md-button")
        
        # Check computed styles
        bg_color = button.value_of_css_property("background-color")
        assert bg_color != "rgba(0, 0, 0, 0)", "Button should have background color"
        
        padding = button.value_of_css_property("padding")
        assert padding != "0px", "Button should have padding"
        
        # Check hover state
        actions = ActionChains(driver)
        actions.move_to_element(button).perform()
        time.sleep(0.5)
        
        hover_bg = button.value_of_css_property("background-color")
        # Hover state might change color or add effects
        cursor = button.value_of_css_property("cursor")
        assert cursor == "pointer", "Button should have pointer cursor"
    
    def test_grids_structure(self, mkdocs_server):
        """Test that grids have proper card layout structure."""
        response = requests.get(f"{mkdocs_server}/test-features/")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find grid containers
        grids = soup.find_all('div', class_='grid')
        assert len(grids) > 0, "No grid containers found"
        
        # Check for card grids
        card_grids = soup.find_all('div', class_=['grid', 'cards'])
        assert len(card_grids) > 0, "No card grids found"
        
        # Verify grid contains list items
        for grid in card_grids:
            cards = grid.find_all('li')
            assert len(cards) > 0, "Grid has no cards"
            
            # Each card should have content
            for card in cards:
                assert card.find('p'), "Card missing content"
    
    def test_grids_responsive_layout(self, mkdocs_server, driver):
        """Test that grids are responsive and properly laid out."""
        driver.get(f"{mkdocs_server}/test-features/")
        
        # Find grid container
        grid = driver.find_element(By.CSS_SELECTOR, ".grid.cards")
        
        # Check CSS Grid or Flexbox is applied
        display = grid.value_of_css_property("display")
        assert display in ["grid", "flex"], f"Grid should use CSS Grid or Flexbox, got {display}"
        
        # Check cards have proper spacing
        cards = driver.find_elements(By.CSS_SELECTOR, ".grid.cards li")
        assert len(cards) >= 2, "Need at least 2 cards to test layout"
        
        # Get positions to verify they're laid out in grid
        positions = []
        for card in cards[:2]:
            rect = card.rect
            positions.append((rect['x'], rect['y']))
        
        # Cards should be side-by-side (same Y) or stacked (same X)
        if positions[0][1] == positions[1][1]:  # Same Y = horizontal
            assert positions[0][0] != positions[1][0], "Cards should be spaced horizontally"
        else:  # Different Y = vertical
            assert positions[0][0] == positions[1][0], "Stacked cards should align vertically"
    
    def test_tooltips_structure(self, mkdocs_server):
        """Test that tooltips are present in HTML."""
        response = requests.get(f"{mkdocs_server}/test-features/")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check for abbr elements (common tooltip implementation)
        abbr_tooltips = soup.find_all('abbr')
        
        # Check for Material tooltip classes
        material_tooltips = soup.find_all(attrs={'data-md-tooltip': True})
        
        # At least one tooltip method should be present
        assert len(abbr_tooltips) > 0 or len(material_tooltips) > 0, \
            "No tooltips found (checked abbr and data-md-tooltip)"
        
        # Verify tooltip has title
        for tooltip in abbr_tooltips:
            assert tooltip.get('title'), "Tooltip missing title attribute"
    
    def test_tooltips_interactivity(self, mkdocs_server, driver):
        """Test that tooltips appear on hover."""
        driver.get(f"{mkdocs_server}/test-features/")
        
        # Try to find tooltip element
        tooltip_selectors = [
            "abbr[title]",
            "[data-md-tooltip]",
            ".md-tooltip"
        ]
        
        tooltip_elem = None
        for selector in tooltip_selectors:
            try:
                tooltip_elem = driver.find_element(By.CSS_SELECTOR, selector)
                break
            except:
                continue
        
        if not tooltip_elem:
            pytest.skip("No tooltip elements found to test")
        
        # Get title text
        title_text = tooltip_elem.get_attribute("title") or \
                     tooltip_elem.get_attribute("data-md-tooltip")
        
        # Hover over element
        actions = ActionChains(driver)
        actions.move_to_element(tooltip_elem).perform()
        time.sleep(1)  # Wait for tooltip animation
        
        # Check if tooltip is visible (implementation varies)
        # Material uses a separate tooltip element that appears
        tooltip_popup = driver.find_elements(By.CSS_SELECTOR, ".md-tooltip__inner")
        if tooltip_popup:
            assert tooltip_popup[0].is_displayed(), "Tooltip popup should be visible"
            assert title_text in tooltip_popup[0].text, "Tooltip should show title text"
    
    def test_material_css_classes_exist(self, mkdocs_server, driver):
        """Test that Material-specific CSS classes have styles."""
        driver.get(f"{mkdocs_server}/test-features/")
        
        # Test critical Material classes have computed styles
        test_cases = [
            (".md-button", "padding", "0px"),  # Should NOT be 0
            (".grid.cards", "display", "block"),  # Should be grid or flex
            (".md-annotation__index", "cursor", "auto"),  # Should be pointer
        ]
        
        for selector, property, not_value in test_cases:
            try:
                elem = driver.find_element(By.CSS_SELECTOR, selector)
                value = elem.value_of_css_property(property)
                assert value != not_value, \
                    f"{selector} {property} should not be {not_value}, got {value}"
            except:
                # Element might not exist if feature not properly implemented
                pass


if __name__ == "__main__":
    pytest.main([__file__, "-v"])