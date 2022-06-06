import csv

f = open('./subtasks.csv', 'w')
writer = csv.writer(f)

startIndex = 4
endIndex = 209
skipIndexes = [204, 205, 206, 207, 208]

jiraPrefix = "GMS"

initialRow = ["Issue Id", "Parent Id", "Summary", "Issue Type", "Assignee", "Reporter"]
writer.writerow(initialRow)

issueIdIterator = 2250

summaryStepOne = "Develop opinionated modules and scripts in Terraform and update the TDD (if applicable)"
summaryStepTwo = "Identify and update existing security application configurations"
summaryStepThree = "Identify existing documentation for related processes and propose changes/revisions to documentation"
summaryStepFour = "Conduct user acceptance testing and validate acceptance criteria"
summaryStepFive = "Sign off on proposed changes to TDD"
summaryStepSix = "Analyze test plans and outcomes relating to compliance considerations"
summaryStepSeven = "Analyze test plans and outcomes relating to regulation considerations"
summaryStepEight = "Analyze test plans and outcomes relating to security posture"
summaryStepNine = "Analyze test plans and outcomes relating to data privacy considerations"
summaryStepTen = "Analyze test plans and outcomes relating to appropriate application security considerations"
summaryStepEleven = "Analyze test plans and outcomes relating to appropriate resilience"
summaryStepTwelve = "Analyze test plans and outcomes relating to IT compliance"

assigneeUnassigned = ""
assigneeStepSix = "E19465"
assigneeStepSeven = "E31642"
assigneeStepEight = "E23028"
assigneeStepNine = "E20034"
assigneeStepTen = "ealdrich"
assigneeStepEleven = "E31216"
assigneeStepTwelve = "E30261"


# Iterate through all of the stories in the board.
for i in range(startIndex, endIndex + 1):
    if i not in skipIndexes:

        issueId = 1000 + issueIdIterator

        # Define row values.
        
        parentId = "GMS-" + str(i)
        issueType = "Sub-task"
        reporter = "E44640"
        
        # Construct the rows in the CSV.
        # rowStepOne = [str(issueId), parentId, summaryStepOne, issueType, assigneeUnassigned, reporter]
        # rowStepTwo = [str(issueId + 1), parentId, summaryStepTwo, issueType, assigneeUnassigned, reporter]
        # rowStepThree = [str(issueId + 2), parentId, summaryStepThree, issueType, assigneeUnassigned, reporter]
        # rowStepFour = [str(issueId + 3), parentId, summaryStepFour, issueType, assigneeUnassigned, reporter]
        # rowStepFive = [str(issueId + 4), parentId, summaryStepFive, issueType, assigneeUnassigned, reporter]
        # rowStepSix = [str(issueId + 5), parentId, summaryStepSix, issueType, assigneeStepSix, reporter]
        # rowStepSeven = [str(issueId + 6), parentId, summaryStepSeven, issueType, assigneeStepSeven, reporter]
        # rowStepEight = [str(issueId + 7), parentId, summaryStepEight, issueType, assigneeStepEight, reporter]
        # rowStepNine = [str(issueId + 8), parentId, summaryStepNine, issueType, assigneeStepNine, reporter]
        # rowStepTen = [str(issueId + 9), parentId, summaryStepTen, issueType, assigneeStepTen, reporter]
        # rowStepEleven = [str(issueId + 10), parentId, summaryStepEleven, issueType, assigneeStepEleven, reporter]
        rowStepTwelve = [str(issueId + 11), parentId, summaryStepTwelve, issueType, assigneeStepTwelve, reporter]


        # Write to the CSV.
        # writer.writerow(rowStepOne)
        # writer.writerow(rowStepTwo)
        # writer.writerow(rowStepThree)
        # writer.writerow(rowStepFour)
        # writer.writerow(rowStepFive)
        # writer.writerow(rowStepSix)
        # writer.writerow(rowStepSeven)
        # writer.writerow(rowStepEight)
        # writer.writerow(rowStepNine)
        # writer.writerow(rowStepTen)
        # writer.writerow(rowStepEleven)
        writer.writerow(rowStepTwelve)

        issueIdIterator += 1

f.close()