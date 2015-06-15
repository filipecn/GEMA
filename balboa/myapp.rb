require 'sinatra'

require './spiders/timus/Timus'

hashusers = {name: "foo"}

class Problem
	attr_accessor :name
end

problem = Problem.new()
problem.name = "BENE"
problem2 = Problem.new()
problem2.name = "BIANCA"

problems = [problem, problem2]

timus = Timus.new
problems = timus.problems
problemSet = {}
problems.collect { |p|
	problemSet[p.tags[0]] = []
}

problems.collect { |p|
	problemSet[p.tags[0]].push(p)
}

get '/timus' do
	problems = timus.problems
	erb :timus, :locals => {:problemSet => problemSet}
end

get '/update' do
	hashusers = {name: "foo"}
	problems = [problem]
	#redirect back
	redirect to("/bianca")
end

get '/:name' do
	erb :index, :locals => {:user => problem, :problems => problems}
end
