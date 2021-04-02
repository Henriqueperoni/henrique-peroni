const projectAnim = gsap.timeline({ defaults: { ease: "power1.out" } });

projectAnim.from("body > div > div:nth-child(1)", { opacity: 0, duration: 2, delay: 0.2});