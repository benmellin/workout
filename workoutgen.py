"""

Data structure:
List, dictionary

Function: workout generator
-randomly selects workout type
-Selects number of activites for workout
-randomly selects activites for workout
-randomly selects number of reps for the wokrout


classes:

class 1: 
	workout type: 
		-attributes: workout type, per round difficulty? need something to quanitfy the difficulty of a round?

class 2: exercise type
- instance attributes: upper, lower body, abs, name, per rep difficulty
-methods:
	getters for each attribute


Overall function:

	We have a total workout difficult number: 1000
	
	First, picks overall workout type

	Next, picks how many rounds or minutes. There is a min and max number of rounds and minutes, randomly picks a number in that range. For time workouts and AMRAPS should have approximately the same round range. Then, multiply range by two or three to get total minutes for amrap

	Next, divides 100/# of rounds or minutes, to get per round or per minute difficutly. 

	Next, sub function: picks three random exercises, and gets their per rep difficulty.

	Next, Sub function: rep chooser: decides how many reps of exercise per minute. If it is an EMOM, we choose one exercise to sum up that per minute difficulty, but if it is FT or amrap, we pick three exercises and difficulties to sum to the per round range. 

	Next, sub funciton: workout builder assembles all the pieces and prints out the proper workout.


"""
import random
import math

class Workout:
	def __init__(self,name, round_range_min, round_range_max,work_multiplier):
		self._name = name
		self._round_range_min = round_range_min
		self._round_range_max = round_range_max
		self._work_multiplier = work_multiplier



class Exercise:

	def __init__(self, type, difficulty,ex_mult,rep_name):
		self._type = type
		self._difficulty = difficulty
		self._ex_mult = ex_mult
		self._rep_name = rep_name

	def set_difficulty(self,difficulty): #for bear crawl
		self.difficulty = difficulty

	def get_difficulty(self):
		return self._difficulty

	def get_type(self):
		return self._type

	def get_rep_number(self,difficulty_needed):
		reps_to_do=math.ceil(difficulty_needed/self._difficulty)
		return reps_to_do



def workout_list_generator():
	work1 = Workout("EMOM", 3,6,3) # Multiply rounds by three to get total rounds
	work2 = Workout("AMRAP", 3,5,3) #multiply by three to get total number of minutes
	work3 = Workout("For Time", 4,7,1) 
	work4 = Workout("Run/Walk", 3,6,5) #multiply by 5 to get total number of minutes

	workout_list = [work1,work2,work3,work4]

	return workout_list

def ex_list_generator():
	ex1 = Exercise("Knee Push Ups", 10,1,"reps")
	ex2 = Exercise("Burpees", 13,1,"reps")
	ex3 = Exercise("Chair Dips",7,1,"reps")
	ex4 = Exercise("Mountain Climbers",7,2,"reps") #difficulty per two reps
	ex5 = Exercise("Bear Crawl", 80,1,"small/medium room lengths")

	ub_ex_list = [ex1,ex2,ex3,ex4,ex5]

	ex6 = Exercise("Plank Shoulder Taps",8,2,"shoulder taps") #difficulty per two reps
	ex7 = Exercise("Sit Ups", 8,1, "reps")
	ex8 = Exercise("Plank Hold", 14,5,"seconds") #difficulty per 5 seconds
	ex9 = Exercise("Bicycle Crunches", 10,2,"reps") #difficulty per two reps
	ex10 = Exercise("Russian Twists", 6,2,"twists") # difficutly per two reps

	ab_ex_list = [ex6,ex7,ex8,ex9,ex10]

	ex11 = Exercise("Air Squats",6,1,"reps") 
	ex12 = Exercise("Squat Jumps", 9,1,"reps")
	ex13 = Exercise("Jumping Lunges", 15,2,"reps") #difficulty per 2 reps
	ex14 = Exercise("Standing Lunges", 9,2,"reps") #difficulty per two reps
	ex15 = Exercise("Stair/Chair Step Ups", 13,2,"reps") # difficutly per two reps

	lb_ex_list = [ex11,ex12,ex13,ex14,ex15]

	return ub_ex_list, ab_ex_list, lb_ex_list 







def level_1_workout_gen():

	l1_ub_ex_list,l1_ab_ex_list,l1_lb_ex_list = ex_list_generator()

	l1_workout_list = workout_list_generator()

	WOD_Type=random.choice(l1_workout_list)

	rounds=random.randint(WOD_Type._round_range_min, WOD_Type._round_range_max)
	

	per_round_difficulty = -50/3*rounds+250

	per_ex_difficulty = per_round_difficulty/3

	rounds=rounds*WOD_Type._work_multiplier

	if WOD_Type._name=="AMRAP":
		rounds=random.randint(rounds, rounds+3)


	ub_ex=random.choice(l1_ub_ex_list)
	ab_ex=random.choice(l1_ab_ex_list)
	lb_ex=random.choice(l1_lb_ex_list)



	ub_ex_reps=ub_ex.get_rep_number(per_ex_difficulty)*ub_ex._ex_mult
	ab_ex_reps=ab_ex.get_rep_number(per_ex_difficulty)*ab_ex._ex_mult
	lb_ex_reps=lb_ex.get_rep_number(per_ex_difficulty)*lb_ex._ex_mult

	ex_list = [[ub_ex,ub_ex_reps],[ab_ex,ab_ex_reps],[lb_ex,lb_ex_reps]]
	random.shuffle(ex_list)

	

	if WOD_Type._name=="Run/Walk":
		return f"Run/Walk for {rounds} minutes"
	elif WOD_Type._name=="For Time":
		return f"{rounds} Rounds for Time: <br><br>{ex_list[0][0]._type}--{ex_list[0][1]} {ex_list[0][0]._rep_name} <br>{ex_list[1][0]._type}--{ex_list[1][1]} {ex_list[1][0]._rep_name}<br>{ex_list[2][0]._type}--{ex_list[2][1]} {ex_list[2][0]._rep_name}"
	elif WOD_Type._name=="EMOM":
		return f"Every Minute On The Minute for {rounds} minutes: <br><br>Minute 1: {ex_list[0][0]._type}--{ex_list[0][1]} {ex_list[0][0]._rep_name} <br>Minute 2: {ex_list[1][0]._type}--{ex_list[1][1]} {ex_list[1][0]._rep_name}<br>Minute 3: {ex_list[2][0]._type}--{ex_list[2][1]} {ex_list[2][0]._rep_name}"
	elif WOD_Type._name=="AMRAP":
		return f"As Many Rounds As Possible in {rounds} minutes: <br><br>{ex_list[0][0]._type}--{ex_list[0][1]} {ex_list[0][0]._rep_name} <br>{ex_list[1][0]._type}--{ex_list[1][1]} {ex_list[1][0]._rep_name}<br>{ex_list[2][0]._type}--{ex_list[2][1]} {ex_list[2][0]._rep_name}"













	






print(level_1_workout_gen())












"""


Workout_Formats=[
["AMRAP",8,15,"minute"],
["EMOM",3,5,"minute"],#multiply by 3
["Walk/Run",4,6,"minutes"],#multiply by 5
["For Time",3,6,"rounds"]
]

upperbody_exercises=[
["Pushups",5,12,"reps"],
["Burpees",3,8,"reps"],
["Chair Dips",8,15,"reps"],
["Mountain Climbers",4,8,"reps"], #multiply number by two
["Bear Crawl", "","","",""] #Not numbered reps
]

ab_exercises=[
["Plank Shoulder Taps",4,8, "reps"],#multiply number by two
["Sit Ups",5,10, "reps"],
["Plank Hold", 3,6,"seconds"], #multiply number by 5
["Bicycle Crunches",5,10,"reps"], #multiply by 2
["Russian Twists", 7,12,"reps"] #multiply by 2
]


lowerbody_exercises=[
["Air Squats",8,16,"reps"],
["Squat Jumps",3,7,"reps"],
["Standing Lunges",3,7,"reps"], #multiply by 2
["Jumping Lunges",2,5,"reps"], #multiply by 2
["Sturdy Chair Step Ups",2,5,"reps"] #multiply by two
]


def workout_generator():
	WOD_Type=random.choice(Workout_Formats)
	rounds=random.randint(WOD_Type[1], WOD_Type[2])
	if WOD_Type[0]=="Walk/Run":
		rounds=rounds*5
		return f"Walk/Run for {rounds} minutes"
	if WOD_Type[0]=="EMOM":
		rounds=rounds*3
	lb=random.choice(lowerbody_exercises)
	ub=random.choice(upperbody_exercises)
	ab=random.choice(ab_exercises)

	lb_reps=random.randint(lb[1], lb[2])

	if ub[0]!="Bear Crawl":
		ub_reps=random.randint(ub[1], ub[2])
		ub_to_print=f"{ub_reps} {ub[3]} of {ub[0]}"
	if ub[0]=="Bear Crawl":
		ub_reps="Across a small or medium room"
		ub_to_print="Bear crawl across a small or medium room"


	ab_reps=random.randint(ab[1], ab[2])

	if lb[0] in ["Standing Lunges","Jumping Lunges","Sturdy Chair Step Ups"]:
		lb_reps=lb_reps*2
	if ub[0] in ["Mountain Climbers"]:
		ub_reps=lb_reps*2
	if ab[0] in ["Standing Lunges","Jumping Lunges","Sturdy Chair Step Ups"]:
		ab_reps=ab_reps*2
	if ab[0]=="Plank Hold":
		ab_reps=ab_reps*5

	ab_to_print=f"{ab_reps} {ab[3]} of {ab[0]}"
	lb_to_print=f"{lb_reps} {lb[3]} of {lb[0]}"

	ex_list=[ab_to_print, lb_to_print, ub_to_print]
	random.shuffle(ex_list)

	if WOD_Type[0]=="EMOM":
		wod_to_print=f"Every minute on the minute for {rounds} minutes: Minute 1: {ex_list[0]}, Minute 2: {ex_list[1]}, Minute 3: {ex_list[2]}"
	
	else:
		if WOD_Type[0]=="For Time":
			wod_to_print=f"For Time: {rounds} rounds of {ex_list[0]}, {ex_list[1]}, {ex_list[2]}"
		if WOD_Type[0]=="AMRAP":
			wod_to_print=f"As many rounds as possible in {rounds} minutes: {ex_list[0]}, {ex_list[1]}, {ex_list[2]}"



 


	return wod_to_print



	

print(workout_generator())
"""




