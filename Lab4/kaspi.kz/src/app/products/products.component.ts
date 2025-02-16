import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PRODUCTS, Product } from './products.data';

@Component({
  selector: 'app-products',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent {
  products: Product[] = PRODUCTS;

  share(link: string) {
    const message = encodeURIComponent(`Посмотри этот товар: ${link}`);
    window.open(`https://t.me/share/url?url=${message}`, '_blank');
  }

  openonkaspi(link: string) {
    window.open(`${link}`, '_blank');
  }
}
