export interface Product {
    image: string;
    name: string;
    description: string;
    rating: number;
    link: string;
  }
  
  export const PRODUCTS: Product[] = [
    {
        image: "./assets/1.1.jpg",
        name: "Palit RTX 5080 Gamerock",
        description: "NE75080019T2-GB2030G 16 Гб",
        rating: 5.0,
        link: "https://kaspi.kz/shop/p/palit-rtx-5080-gamerock-ne75080019t2-gb2030g-16-gb-134261517/?c=750000000" 
      },
    {
      image: "./assets/1.2.jpg",
      name: "Palit GeForce RTX 3060 Dual",
      description: "NE63060019K9-190AD 12GB",
      rating: 5.0,
      link: "https://kaspi.kz/shop/p/palit-geforce-rtx-3060-dual-ne63060019k9-190ad-12gb-101214928/?c=750000000" 
    },
    {
        image: "./assets/1.3.jpg",
        name: "ASUS RTX 4070 Ti Super ",
        description: "TUF Gaming OC 16 Гб",
        rating: 5.0,
        link: "https://kaspi.kz/shop/p/asus-rtx-4070-ti-super-tuf-gaming-oc-16-gb-117054530/?c=750000000"
      },
    {
        image: "./assets/1.4.jpg",
        name: "GIGABYTE GeForce RTX 3050 Windforce",
        description: "OC GV-N3050WF2OC-6GD 6 Гб",
        rating: 3.9,
        link: "https://kaspi.kz/shop/p/gigabyte-geforce-rtx-3050-windforce-oc-gv-n3050wf2oc-6gd-6-gb-119935068/?c=750000000" 
      },
    {
        image: "./assets/1.5.jpg",
        name: "AFOX RX 580",
        description: "AFRX580-8192D5H3-V3 8 Гб",
        rating: 5.0,
        link: "https://kaspi.kz/shop/p/peladn-radeon-rx-580-8-gb-110566490/?c=750000000"
      }
  ];
  