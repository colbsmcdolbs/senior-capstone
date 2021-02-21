import { Component, OnInit, Pipe } from '@angular/core';
import { Form } from '../interfaces/form';
import { Races, Workclasses, Educations, Relationships, MaritalStatuses, Genders, Occupations, NativeCountries } from '../data/form-data';
import { SelectOption } from '../interfaces/select-option';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-model-form',
  templateUrl: './model-form.component.html',
  styleUrls: ['./model-form.component.css']
})
export class ModelFormComponent implements OnInit {

  public modelForm: Form;
  public fullName: string = '';
  public message: string;
  public isFormLocked: boolean = false;

  public races: SelectOption[] = Races;
  public workclasses: SelectOption[] = Workclasses;
  public educations: SelectOption[] = Educations;
  public relationships: SelectOption[] = Relationships;
  public maritalStatuses: SelectOption[] = MaritalStatuses;
  public genders: SelectOption[] = Genders;
  public occupations: SelectOption[] = Occupations;
  public nativeCountries: SelectOption[] = NativeCountries;
  public ageRange: number[] = [];
  public workHoursRange: number[] = [];

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.modelForm = { age: null, education: null, gender: null, hoursPerWeek: null, 
      maritalStatus: null, nativeCountry: null, occupation: null, race: null, relationship: null,
      workclass: null };

    this.nativeCountries.sort((a, b) => a.value.localeCompare(b.value)); // Sort our Native Countries
    this.occupations.sort((a, b) => a.value.localeCompare(b.value));

    for (let i = 18; i < 101; i++) this.ageRange.push(i);
    for (let i = 0; i < 81; i++) this.workHoursRange.push(i);
  }

  public async onSubmit(formData: any) {
    const response = await this.apiService.submitForm(formData.value);
    if (response.error){ 
      this.message = `Error Retrieving Results. Error: '${response.error}`;
    } else {
      const result = response.result[0];
      this.message = (result === 0) 
                      ? `${this.fullName} DOES qualifies for financial assistance.`
                      : `${this.fullName} does NOT qualify for financial assistance.`;
      this.isFormLocked = true;
    }
  }

  public clearForm(): void {
    const tempObject = {};
    this.modelForm = tempObject;
    this.fullName = '';
    this.isFormLocked = false;
  }
}
