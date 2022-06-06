# Bulk Jira Upload - ConfigMgmt

To bulk upload sub-tasks to Jira, you need to provide a prepared CSV file to the ConfigMgmt group. This repository provides a simple Python script to generate the CSV programmatically.

## Description

Each sub-task in Jira requires a set of fields to be defined in order to create them in the GMS project. Once these standard values are provided and indeces filled, the Excel sheet will generate a list of rows in a CSV that you can provide to the ConfigMgmt team for a bulk upload to the Jira project.

## Instructions

1. Fill out the indexes to reflect which set of stories you want the sub-task created for.
2. Fill out the summary and assignee fields for each of the sub-tasks you with to add to all of the Jira stories defined in Step 1.
3. Add a block of code (or leverage one of the existing blocks of code) to generate the row and write to the CSV. Comment out other lines of code for sub-tasks which you don't wish to add.

## Support

Please contact [Arnav Jain](mailto:arnjain@deloitte.com) with any questions.
Code last updated on June 6, 2022.

