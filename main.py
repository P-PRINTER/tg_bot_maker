import dotenv
import os

import interface


if __name__ == '__main__':
	
	dotenv.load_dotenv()

	TOKEN	= os.getenv('API_TOKEN')
	interface.make.run_bot(TOKEN)