import dotenv
import os

from interface import make


if __name__ == '__main__':
	
	dotenv.load_dotenv()

	TOKEN	= os.getenv('API_TOKEN')
	make.run_bot(TOKEN)