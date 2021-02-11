import { Component, OnInit, Pipe } from '@angular/core';
import { Form } from '../interfaces/form';
import { Races, Workclasses, Educations, Relationships, MaritalStatuses, Genders, Occupations, NativeCountries } from '../data/form-data';
import { SelectOption } from '../interfaces/select-option';
import { ApiService } from '../services/api.service'
import { convertTypeAcquisitionFromJson } from 'typescript';

@Component({
  selector: 'app-model-form',
  templateUrl: './model-form.component.html',
  styleUrls: ['./model-form.component.css']
})
export class ModelFormComponent implements OnInit {

  public modelForm: Form;
  public fullName: string;
  public formSubmitted: boolean = false;

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
    this.fullName = '';
    this.nativeCountries.sort((a, b) => a.value.localeCompare(b.value)); // Sort our Native Countries
    this.occupations.sort((a, b) => a.value.localeCompare(b.value));

    for (let i = 18; i < 101; i++) this.ageRange.push(i);
    for (let i = 0; i < 81; i++) this.workHoursRange.push(i);

    console.log(this.ageRange)
  }

  async onSubmit(formData: any) {
    this.formSubmitted = true;
    const response = await this.apiService.submitForm(formData.value);
    console.log(response);
  }

  public clearForm(): void {
    this.formSubmitted = false;
    const tempObject = {};
    this.modelForm = tempObject;
    this.fullName = '';
  }

}