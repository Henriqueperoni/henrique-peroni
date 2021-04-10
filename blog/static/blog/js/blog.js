const postAnim = gsap.timeline({ defaults: { ease: "power1.out" } });

postAnim.from(".post", { opacity: 0, duration: .6, stagger: 0.3 });