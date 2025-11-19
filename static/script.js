// Wait until the HTML is fully loaded before running the script
document.addEventListener('DOMContentLoaded', function() {

    // ==========================================
    // 1. MOBILE MENU LOGIC
    // ==========================================
    
    const menuButton = document.getElementById('mobile-menu-button');
    const closeButton = document.getElementById('mobile-close-button');
    const mobileNav = document.getElementById('mobile-nav');
    const overlay = document.getElementById('mobile-menu-overlay');

    function openMenu() {
        document.body.classList.add('mobile-nav-open');
        if(menuButton) menuButton.setAttribute('aria-expanded', 'true');
    }

    function closeMenu() {
        document.body.classList.remove('mobile-nav-open');
        if(menuButton) menuButton.setAttribute('aria-expanded', 'false');
    }

    if (menuButton && mobileNav) {
        menuButton.addEventListener('click', openMenu);
    }

    if (closeButton && mobileNav) {
        closeButton.addEventListener('click', closeMenu);
    }

    if (overlay) {
        overlay.addEventListener('click', closeMenu);
    }

    if (mobileNav) {
        mobileNav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function(event) {
                // Only close menu if it's an anchor link to a section or page
                const href = this.getAttribute('href');
                if (href) {
                    // Allow default behavior (navigation) but close menu first
                    closeMenu(); 
                }
            });
        });
    }

    // ==========================================
    // 2. TYPEWRITER EFFECT LOGIC
    // ==========================================

    const words = [
        "Custom Business Websites.", 
        "Python Backends.", 
        "Workflow Automations.", 
        "Secure Client Portals.", 
        "Scalable Web Apps."
    ];
    
    let i = 0;
    let timer;

    function typeWriter() {
        const heading = document.querySelector(".typewriter-text");
        // If the element isn't found (e.g., on a different page), stop here
        if (!heading) return;
        
        const word = words[i];
        let charIndex = 0;
        let isDeleting = false;

        function loop() {
            // Update the text content
            heading.innerHTML = word.substring(0, charIndex);
            
            // Logic to determine if we are typing or deleting
            if (isDeleting) {
                charIndex--;
            } else {
                charIndex++;
            }

            // Control the speed and direction
            if (!isDeleting && charIndex > word.length) {
                // Finished typing word, wait 2 seconds then start deleting
                isDeleting = true;
                setTimeout(loop, 2000); 
            } else if (isDeleting && charIndex === 0) {
                // Finished deleting, move to next word
                isDeleting = false;
                i = (i + 1) % words.length;
                // Wait 0.5s before typing next word
                setTimeout(typeWriter, 500);
            } else {
                // Typing speed (100ms) vs Deleting speed (50ms)
                setTimeout(loop, isDeleting ? 50 : 100);
            }
        }

        // Start the loop for the current word
        loop();
    }

    // Start the typewriter effect
    typeWriter();

    // ==========================================
    // 3. SCROLL & INTERACTIVE UI FEATURES
    // ==========================================

    // We attach the scroll event to the window
    window.onscroll = function() {
        handleScrollEffects();
    };

    function handleScrollEffects() {
        // --- Back To Top Button Visibility ---
        const backToTopBtn = document.getElementById("back-to-top");
        if (backToTopBtn) {
            // Show button after scrolling down 300px
            if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
                backToTopBtn.classList.add("visible");
            } else {
                backToTopBtn.classList.remove("visible");
            }
        }
    }

    // --- Back To Top Click Event ---
    const backToTopBtn = document.getElementById("back-to-top");
    if (backToTopBtn) {
        backToTopBtn.addEventListener("click", function() {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });
    }
    
    // ==========================================
    // 4. INTERACTIVE FAQ (Solutions Page)
    // ==========================================
    // This exposes the toggle function globally so the HTML 'onclick' works
    window.toggleFaq = function(element) {
        element.classList.toggle("active");
    };

});