const introAnim = gsap.timeline({defaults: {ease: 'power1.out'}})

introAnim.to(".greeting", { y: "0%", duration: 1, delay: 0.2, stagger: 0.4 });
introAnim.fromTo(".intro-image", { y: "50%", opacity: 0 }, { y: "0%", opacity: 1, duration: 1}, "=-1");
