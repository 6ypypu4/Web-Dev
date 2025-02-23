import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AppService } from '../app.service';
import { ProductItemComponent } from '../product-item/product-item.component';
import { NgFor } from '@angular/common';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports:   [NgFor, ProductItemComponent],
  templateUrl: `product-list.component.html`,
  styleUrl: `product-list.component.css`,
})
export class ProductListComponent implements OnInit {
  products: any[] = [];

  constructor(private route: ActivatedRoute, private appService: AppService) {}

  ngOnInit() {
    this.route.paramMap.subscribe((params) => {
      const categoryId = Number(params.get('id')) as 1 | 2 | 3 | 4;
      this.products = this.appService.getProductsByCategory(categoryId);
    });
  }

  removeProduct(id: number) {
    this.products = this.products.filter((product) => product.id !== id);
  }

  likeProduct(product: any) {
    product.likes++;
  }
}
