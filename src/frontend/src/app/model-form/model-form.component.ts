import { Component, OnInit, Pipe } from '@angular/core';
import { Form } from '../interfaces/form';
import { Races, Workclasses, Educations, Relationships, MaritalStatuses, Genders, Occupations, NativeCountries } from '../data/form-data';
import { SelectOption } from '../interfaces/select-option';
import { ApiService } from '../services/api.service'

@Component({
  selector: 'app-model-form',
  templateUrl: './model-form.component.html',
  styleUrls: ['./model-form.component.css']
})
export class ModelFormComponent implements OnInit {

  public modelForm: Form;
  public fullName: string;
  private formSubmitted: boolean;

  public races: SelectOption[] = Races;
  public workclasses: SelectOption[] = Workclasses;
  public educations: SelectOption[] = Educations;
  public relationships: SelectOption[] = Relationships;
  public maritalStatuses: SelectOption[] = MaritalStatuses;
  public genders: SelectOption[] = Genders;
  public occupations: SelectOption[] = Occupations;
  public nativeCountries: SelectOption[] = NativeCountries;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.fullName = "";
    this.nativeCountries.sort((a, b) => a.value.localeCompare(b.value)); // Sort our Native Countries
    this.occupations.sort((a, b) => a.value.localeCompare(b.value));
  }

  onSubmit() {
    this.formSubmitted = true;
    console.log(this.modelForm);
  }

}