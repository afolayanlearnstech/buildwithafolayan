// Wait until the HTML is fully loaded before running the script
document.addEventListener('DOMContentLoaded', function() {

    // Find the hamburger button, the close button, and the mobile nav menu
    const menuButton = document.getElementById('mobile-menu-button');
    const closeButton = document.getElementById('mobile-close-button');
    const mobileNav = document.getElementById('mobile-nav');

    // Function to open the menu
    function openMenu() {
        mobileNav.classList.add('mobile-nav-open'); 
        // Optional: Disable scrolling on the body when menu is open
        document.body.style.overflow = 'hidden'; 
    }

    // Function to close the menu
    function closeMenu() {
        mobileNav.classList.remove('mobile-nav-open');
        // Optional: Re-enable scrolling
        document.body.style.overflow = ''; 
    }

    // Add event listener to the hamburger button
    if (menuButton && mobileNav) { // Check if elements exist
        menuButton.addEventListener('click', openMenu);
    }

     // Add event listener to the close button
    if (closeButton && mobileNav) { // Check if elements exist
        closeButton.addEventListener('click', closeMenu);
    }

    // Optional: Close the menu if a link inside it is clicked
    if (mobileNav) {
        mobileNav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', closeMenu);
        });
    }

});