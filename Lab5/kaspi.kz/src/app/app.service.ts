import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class AppService {
  categories = ['GPU', 'CPU', 'RAM', 'SSD'];

  products = {
    1: [
      {
        id: 1,
        name: 'Palit RTX 5080 Gamerock',
        likes: 0,
        image: './assets/1.1.jpg',
        description: 'NE75080019T2-GB2030G 16 Гб',
        rating: 5.0,
        link: 'https://kaspi.kz/shop/p/palit-rtx-5080-gamerock-ne75080019t2-gb2030g-16-gb-134261517/?c=750000000'
      },
      {
        id: 2,
        name: 'Palit GeForce RTX 3060 Dual',
        likes: 0,
        image: './assets/1.2.jpg',
        description: 'NE63060019K9-190AD 12GB',
        rating: 5.0,
        link: 'https://kaspi.kz/shop/p/palit-geforce-rtx-3060-dual-ne63060019k9-190ad-12gb-101214928/?c=750000000'
      },
      {
        id: 3,
        name: 'ASUS RTX 4070 Ti Super',
        likes: 0,
        image: './assets/1.3.jpg',
        description: 'TUF Gaming OC 16 Гб',
        rating: 5.0,
        link: 'https://kaspi.kz/shop/p/asus-rtx-4070-ti-super-tuf-gaming-oc-16-gb-117054530/?c=750000000'
      },
      {
        id: 4,
        name: 'GIGABYTE GeForce RTX 3050 Windforce',
        likes: 0,
        image: './assets/1.4.jpg',
        description: 'OC GV-N3050WF2OC-6GD 6 Гб',
        rating: 3.9,
        link: 'https://kaspi.kz/shop/p/gigabyte-geforce-rtx-3050-windforce-oc-gv-n3050wf2oc-6gd-6-gb-119935068/?c=750000000'
      },
      {
        id: 5,
        name: 'AFOX RX 580',
        likes: 0,
        image: './assets/1.5.jpg',
        description: 'AFRX580-8192D5H3-V3 8 Гб',
        rating: 5.0,
        link: 'https://kaspi.kz/shop/p/peladn-radeon-rx-580-8-gb-110566490/?c=750000000'
      }
    ],
    2: [
      { id: 1, name: 'CPU 1', likes: 0 },
      { id: 2, name: 'CPU 2', likes: 0 },
      { id: 3, name: 'CPU 3', likes: 0 },
      { id: 4, name: 'CPU 4', likes: 0 },
      { id: 5, name: 'CPU 5', likes: 0 }
    ],
    3: [
      { id: 1, name: 'RAM 1', likes: 0 },
      { id: 2, name: 'RAM 2', likes: 0 },
      { id: 3, name: 'RAM 3', likes: 0 },
      { id: 4, name: 'RAM 4', likes: 0 },
      { id: 5, name: 'RAM 5', likes: 0 }
    ],
    4: [
      { id: 1, name: 'SSD 1', likes: 0 },
      { id: 2, name: 'SSD 2', likes: 0 },
      { id: 3, name: 'SSD 3', likes: 0 },
      { id: 4, name: 'SSD 4', likes: 0 },
      { id: 5, name: 'SSD 5', likes: 0 }
    ]
  };

  getCategories() {
    return this.categories;
  }

  getProductsByCategory(id: 1 | 2 | 3 | 4) {
    return this.products[id] || [];
  }
}
