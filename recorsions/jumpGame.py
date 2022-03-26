# simple recursive python script 
def recorsive(curS,indx=0):
    global bestS
    global nums
    curS.append(nums[indx])
    if(indx == (len(nums)-1)):  #reached the end of the way
        if(len(curS) < len(bestS) or (len(bestS)==0)):
            bestS = curS
    elif(( nums[indx] + indx) > (len(nums)-1)):  #reached one step befor the end
        recorsive(curS[:],len(nums)-1)
    else:                                       #have more than one step - check all options
        for x in range (1,nums[indx]+1):
            recorsive(curS[:],indx+x)

nums = [7,3,0,0,0,4,1,2,1,1,1,4,2,1,0]   #input array
bestS = []                               #Sulotion arry
if nums:                                 #Validate input array is not empty
    recorsive([])
print ("Sulotion: ", bestS, " @ ",len(bestS), " Jumps")
