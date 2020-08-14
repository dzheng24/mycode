#!/usr/bin/env python3

import requests ## 3rd party URL lookup

## define the main function
def main():

    custom_start = input("Please enter a start date in this format: yyyy-mm-dd: ")
    custom_end = input("Please enter an end date in this format: yyyy-mm-dd, or enter q to use default option ")
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = '&start_date=' + custom_start  ## start date for data
    enddate = '&end_date=' + custom_end ## create a mechanism to utilize enddate
    mykey = '&api_key=4xjsmaDwVz2AEElARiYEoRaqKp3VHOhHLF5usJuy' ## replace this with our API key

    if custom_end == "q":
         neourl = neourl + startdate + mykey
    else:
         neourl = neourl + startdate + enddate + mykey
   
    neojson = (requests.get(neourl)).json()

    print(neojson)

## call main
main()

