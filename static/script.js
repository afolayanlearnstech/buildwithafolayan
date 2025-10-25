// Wait until the HTML is fully loaded before running the script
document.addEventListener('DOMContentLoaded', function() {

    // Find the hamburger button, the close button, the mobile nav menu, and the new overlay
    const menuButton = document.getElementById('mobile-menu-button');
    const closeButton = document.getElementById('mobile-close-button');
    const mobileNav = document.getElementById('mobile-nav');
    const overlay = document.getElementById('mobile-menu-overlay'); // Get the overlay

    // Function to open the menu
    function openMenu() {
        // Add class to the BODY. This controls everything:
        // 1. The nav sliding in
        // 2. The overlay fading in
        // 3. The hamburger icon animating
        // 4. Disabling body scroll
        document.body.classList.add('mobile-nav-open');
        
        // Update ARIA attribute for accessibility
        menuButton.setAttribute('aria-expanded', 'true');
    }

    // Function to close the menu
    function closeMenu() {
        // Remove class from the BODY
        document.body.classList.remove('mobile-nav-open');
        
        // Update ARIA attribute for accessibility
        menuButton.setAttribute('aria-expanded', 'false');
    }

    // Add event listener to the hamburger button
    if (menuButton && mobileNav) { // Check if elements exist
        menuButton.addEventListener('click', openMenu);
    }

     // Add event listener to the close button
    if (closeButton && mobileNav) { // Check if elements exist
        closeButton.addEventListener('click', closeMenu);
    }

    // --- NEW: Add event listener to the overlay to close menu ---
    if (overlay) {
        overlay.addEventListener('click', closeMenu);
    }

    // --- This section is still correct and essential ---
    // It handles closing the menu *before* navigating to a new page.
    if (mobileNav) {
        mobileNav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function(event) {
                // 1. Prevent the link from navigating immediately
                event.preventDefault(); 
                
                // 2. Get the destination URL from the link
                const href = this.href; 
                
                // 3. Close the menu (which removes the 'mobile-nav-open' class)
                closeMenu(); 
                
                // 4. Wait for the menu's close animation (300ms) to finish
                setTimeout(() => {
                    // 5. Go to the new page
                    window.location.href = href;
                }, 300); // This duration MUST match your CSS transition time
            });
        });
    }

});
