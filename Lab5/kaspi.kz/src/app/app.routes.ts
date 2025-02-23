import { Routes } from '@angular/router';
import { ProductListComponent } from './product-list/product-list.component';

export const routes: Routes = [
    { path: '', redirectTo: '/category/1', pathMatch: 'full' },
    { path: 'category/:id', component: ProductListComponent },
  ];