const navSlide = () => {
    const burger = document.querySelector(".burger")
    const nav = document.querySelector(".nav-links")
    const navLinks = document.querySelectorAll(".nav-links li")

    burger.addEventListener("click", () => {

        // Toggle Navbar
        nav.classList.toggle("nav-active")

        // Animate Each li
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = ''
            } else {
                link.style.animation = `navLinksFade 0.5s ease forwards ${index / 7 + .4}s`
            }
        })

        // Burger Animation
        burger.classList.toggle("close-burger")

    });

}

navSlide()

// Close message container
function closeMessage() {
    const message = document.querySelector(".message-container")
    message.classList.add('delete-message')
    console.log('close')
};

const closeMessageBtn = document.querySelector(".close-message")

if (closeMessageBtn) {
    closeMessageBtn.addEventListener("click", () => {
        closeMessage()
    })
};

// Add Active Navigation Class Based on URL
// Adapt from https://stackoverflow.com/a/58308441
(function () {
    let current = location.pathname.split('/');
    let aboutItem = document.querySelector('nav > ul > li:nth-child(1) > a')

    if (current.length === 3) {
        current = current[1]
    } else {
        aboutItem.classList.add("nav-item-active")
    }
    
    let menuItems = document.querySelectorAll('.nav-links a');
    for (var i = 0, len = menuItems.length; i < len; i++) {
        if (menuItems[i].getAttribute("href").indexOf(current) !== -1) {
            menuItems[i].className += "nav-item-active";
        }
    }
})();
