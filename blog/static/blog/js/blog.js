const postAnim = gsap.timeline({ defaults: { ease: "power1.out" } });

postAnim.to(".post", { opacity: 1, duration: .6, stagger: 0.3 });