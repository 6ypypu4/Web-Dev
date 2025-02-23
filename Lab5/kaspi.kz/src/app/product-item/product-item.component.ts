import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-product-item',
  standalone: true,
  imports: [CommonModule],
  templateUrl: `app-product-item.html`,
  styleUrl: `app-product-item.css`
})
export class ProductItemComponent {
  @Input() product: any;
  @Output() like = new EventEmitter<void>();
  @Output() remove = new EventEmitter<void>();

  onLike() {
    this.like.emit();
  }

  onRemove() {
    this.remove.emit();
  }
}
