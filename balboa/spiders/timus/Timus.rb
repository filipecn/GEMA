#retrieve all problems from acm.timus.ru, categorized and sorted by dificulty
require 'rubygems'
require 'nokogiri'
require 'open-uri'

#require_relative '../Problem'
require './spiders/Problem'

TIMUS_ID = 0

DB = "./spiders/timus/offline/problem_set"

class Timus

	@problemSet

	def problems
		@problemSet
	end

	def initialize
		@problemSet = []

		if File.file?(DB)
			@problemSet = Marshal::load(File.open(DB, "r").read)
		else
			tags = ["structure","dynprog","game","geometry","graphs","hardest",
	   "numbers","beginners","string","tricky","unusual"];

			tags.collect{ |tag|
				page = Nokogiri::HTML(
					open("http://acm.timus.ru/problemset.aspx?space=1&tag=" + 
					     tag + "&skipac=False&sort=difficulty"))

				#page = Nokogiri::HTML(File.open("offline/test", "r").read)

				problemList = page.css(".problemset").css(".content")
				problemListSize = problemList.length

				for i in 1..problemListSize-1
					p = Problem.new
					p.judge = TIMUS_ID
					p.judge_id = problemList[i].css("td")[1].text 
					p.name = problemList[i].css(".name").text
					p.link = problemList[i].css("a")[0]['href']
					p.source = problemList[i].css(".source").text
					p.tags = [tag]
					problems.push(p)
				end
			}

			File.open(DB, "w"){ |file| file.write(Marshal::dump(@problemSet)) }
		end

		#puts @problemSet.inspect
	end

end
