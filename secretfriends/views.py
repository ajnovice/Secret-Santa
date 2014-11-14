from django.shortcuts import render,render_to_response
from secretfriends.models import unique_list
from django.template import RequestContext
import random
import hashlib

# Create your views here.

def friends(request):
    """
    if the request is POST, then extract the string and convert it into list and remove the duplicated spaces  and convert it into lowercase
    and store it in lower_case_list.First see if the given set of names already been used or not. if given set of name is being used for the
    first time then store SHA of the set and its corresponding secret friends set's SHA in database.If its being already used then update the SHA 
    of the new secret friend set in database
    """
    if request.method == "POST":
	string= request.POST["q"]
	new_list=string.split(",")
	secret_list = []
	new_list.sort()

	lower_case_list = []
	for i in range(len(new_list)):
	    lower_case_list.append(" ".join(new_list[i].strip().lower().split()))
	    
	    
	all_ready_stored = unique_list.objects.filter(sha = hashlib.sha1(str(lower_case_list)).hexdigest())
	if not all_ready_stored:
	    for i in range(len(new_list)):
		random_number=random.randint(0,len(new_list)-1)
		while random_number==i:
		    random_number=random.randint(0,len(new_list)-1)
		secret_list.append(new_list[random_number])
	    q=unique_list(sha=hashlib.sha1(str(new_list)).hexdigest(),unique_sha=hashlib.sha1(str(secret_list)).hexdigest())
	    q.save()
	else:
	    all_ready_stored_unique_sha = unique_list.objects.filter(unique_sha = hashlib.sha1(str(lower_case_list)).hexdigest()).values('unique_sha')
	    for i in range(len(new_list)):
		random_number=random.randint(0,len(new_list)-1)
		while random_number==i:
		    random_number=random.randint(0,len(new_list)-1)
		secret_list.append(new_list[random_number])
	    while all_ready_stored_unique_sha == hashlib.sha1(str(secret_list)).hexdigest():
		for i in range(len(new_list)):
		    random_number=random.randint(0,len(new_list)-1)
		    while random_number==i:
			random_number=random.randint(0,len(new_list)-1)
		    secret_list.append(new_list[random_number])
	    
	    unique_list.objects.filter(sha = hashlib.sha1(str(new_list)).hexdigest()).update(unique_sha=hashlib.sha1(str(secret_list)).hexdigest())
	return render_to_response('secretfriends.html',{'zipped_data':zip(new_list,secret_list),},context_instance = RequestContext(request))
	
    if request.method == "GET":
	return render(request,'secretfriends.html')