def getLowestCommonManager(topManager, reportOne, reportTwo):
    #Name: Get Lowest Common Manager
    #Category and difficulty: Recursion, Hard
    #time: O(n) where n is the number of nodes in the graph
    #space: O(h) where h is height of hierarchy
    pathsToReports = []
    getPathToReport(reportOne, topManager, [], pathsToReports)
    getPathToReport(reportTwo, topManager, [], pathsToReports)
    path1 = pathsToReports[0]
    path2 = pathsToReports[1]
    
    currentCommonManagerName = path1[0]
    for index in range(min(len(path1), len(path2))):
        if(path1[index] == path2[index]):
            currentCommonManagerName = path1[index]
        else:
            break

    return currentCommonManagerName

def getPathToReport(report, topManager, path, allPaths):
    print("running for " + topManager.name)
    newPath = path + [topManager] 
    if(report == topManager):
        allPaths.append(newPath)
        return
        
    if(len(allPaths) < 2):
        for directReport in topManager.directReports:
            getPathToReport(report, directReport, newPath, allPaths)
    
# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
