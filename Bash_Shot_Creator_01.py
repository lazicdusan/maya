import argparse
import os

# how to run the code, 1 path to script, 2 shot count, 3 -d folder
# D:\Dusan\Stvaralastvo\Skripte\Bash_Shot_Creator_01.py 5 -d D:\test_folder_script\

#define the main function with all the arguments
def main():
	#help argument
	parser = argparse.ArgumentParser(description='This is a folder shot creator',
		usage='To create shots folder structure')
	
	parser.add_argument('shotCount',help='The number of shots') #first argument shotCount

	parser.add_argument('-d', '--destination', help='If you want to change the default location') #additional argument

	args = parser.parse_args() #needed to parse arguments

	create_files(args.shotCount,destination=args.destination) #call the function with the arguments 

#define the other function
def create_files(shotCount,destination=None):

	#check if the file is given
	if destination:
		#check if it exists and if not make it
		if os.path.isdir(destination):
			pass
		else:
			os.mkdir(destination)
	else:
		raise RuntimeError ('Please give the destination')

	if shotCount.isdigit(): #if the file is a digit
		if (os.listdir(destination)) == []: #if the folder is empty
			for shot in range(int(shotCount)): #number of shots
				shot_number = (shot*10+10) #get the 0 out and numbers from 1 become 10 
				shot_number_reformated = 'SH' + ('%0.3d'  % shot_number) #put SH prefix and reformat to 3 digits 
				shot_folder = os.mkdir(os.path.join(destination,shot_number_reformated)) #create the folders
				shot_folder = os.path.join(destination,shot_number_reformated) #redeclare the variable with the path 
				inside_shot_folders = ['scenes','images','sourceimages'] #possible folders inside shots
				#create inside_shot_folders in the shot folders
				for folder in inside_shot_folders:
					os.mkdir(os.path.join(shot_folder,folder))
		else:
			raise RuntimeError ('The folder contains files')
	else:
		raise RuntimeError ('The input shot count is not a number')

#call the main function
if __name__ == '__main__':
	main()