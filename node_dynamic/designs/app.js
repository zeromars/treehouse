//Problem: we need a simple way to look at a users badge count and javascript points from a web browser.
//Solution: use nodejs to preform the profile lookups and serve our templates via http.

// 1.) Create a webserver

// 2.) Handle http route GET / and POST i.e. Home
	//if url == "/" and GET
		//show search
	//if url is "/" and POST
		//redirect to /:username

// 3.) Handle http route GET /:username i.e. landonlung
	// if url == "/...."
		//get json from treehouse
		//on end
			//show profile
		//on error 
			//show error

// 4.) Function that handles the reading of files and merge in values.
	//read from file and get a string
		// merge values into string