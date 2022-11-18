from jinja2 import Environment, FileSystemLoader
import yaml
import sys

def processTemplate(para):
#  if  str(sys.argv[1]) == "--ec2":
#   print("test worked")
	pfile=str(sys.argv[1])
	config = yaml.full_load(open("parameters/"+pfile))
	template_file=config.get('template')
	template_loc="templates/"+template_file+".yml"
	#template_file=pfile.split("-", 1)[0]
	#rname1=rname[0]
	#pfile=str(sys.argv[2])
	#print(rname)
	#print(pfile)
	f = open("output/"+template_file+".template","a")
	env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
	template = env.get_template(template_loc)
	f.write(template.render(config))
	f.close()

def help():
	print ("Usage:")
	print ("templ.py sns parameter-file.yml\n")

def main():
	if len(sys.argv) < 2:
		help()
	else:
		processTemplate(str(sys.argv[1]))
		#print(str(sys.argv[1])+" "+str(sys.argv[2]))	
if __name__ == "__main__":
	main()
