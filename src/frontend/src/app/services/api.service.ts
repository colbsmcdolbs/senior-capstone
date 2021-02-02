import { Injectable } from '@angular/core';
import { AuthLevel } from './auth.enum';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor() { }

  public getThreshold(): number {
    return null;
  }

  public setThreshold(newValue: number): number {
    // PULL AUTHLEVEL OUT OF SESSION STORAGE
    return null;
  }

  public tryLogin(): AuthLevel {
    return null;
  }

  public logout(): void {
    //REMOVE AUTHLEVEL FROM SESSION STORAGE
  }

  public submitForm() {

  }

  private validateForm() {
    
  }
}
