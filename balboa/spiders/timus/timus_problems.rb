#retrieve all problems from acm.timus.ru, categorized and sorted by dificulty
require 'rubygems'
require 'nokogiri'
require 'open-uri'

require '../Problem'

DB = "offline/"

tags = Array["structure","dynprog","game","geometry","graphs","hardest",
	     "numbers","beginners","string","tricky","unusual"];

tags.collect{ |tag|
	if File.file?(DB + tag) 
		page = Nokogiri::HTML(File.open(DB + tag, "r").read)

	else
		page = Nokogiri::HTML(open("http://acm.timus.ru/problemset.aspx?space=1&tag=" + 
					   tag + "&skipac=False&sort=difficulty"))
		
		problemList = page.css(".problemset").css(".content")
		problemListSize = problemList.length

		File.open(DB + tag, 'a+') { |file| file.write("your text") }
		for i in 1..problemListSize-1
			puts problemList[i].css(".name").text
		end

	end
}

