import { Component } from '@angular/core';
// import * as fs1 from 'fs';
// import * as fs from "fs";
import { observable } from 'rxjs'
import * as propertiesNames from '../../../../../AppData/Local/Programs/Python/Python39/combined.json';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'prototype';
  output: any;
  public lists: any;
  name: string;
  benchNo: any;
  order: any;
  mobileNumber: any;
  items: any;
  totalCost: any;
  tax: any;

  constructor() {

    this.lists = propertiesNames;
    console.log(this.lists);
    this.name = Object.keys(this.lists["default"])[0];
    this.benchNo = this.lists["default"][this.name].BenchNo;
    this.mobileNumber = '+91-' + this.lists["default"][this.name]["Mobile Number"];
    this.items = this.lists["default"][this.name]["Order"];
    this.totalCost = this.lists["default"][this.name]["Total cost"]
    this.tax = (this.totalCost * 10) / 100;
    this.totalCost += this.tax;
    console.log(this.benchNo, this.mobileNumber);
    console.log(Object.keys(this.lists["default"])[0]);
    // console.log(Object.values(this.lists));
    // this.output = Object.values(this.lists)[0];
    // this.createFile();
    // this.showFile();

  }

  // createFile() {

  //   fs.writeFileSync('file.txt', 'I am cool!');
  //   closeSync(fs1);
  //   fs1.close();
  // }

  // showFile() {

  // console.log(fs.readFileSync('file.txt', "utf8"));
  // readFileSync('file.txt', function (err, data) {
  //   if (err) {
  //     return console.error(err);
  //   }
  //   console.log("Asynchronous read: " + data.toString());
  // });
  // }
  // createFile() {
  //   let filehandle;
  //   let newFile = new Blob([this.output], {type: "fi/plain", endings: 'native'});

  // }
  // console.dir(list);
}
