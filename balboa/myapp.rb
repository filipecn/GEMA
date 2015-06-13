require 'sinatra'

hashusers = {name: "foo"}


class Problem
	attr_accessor :name
end

problem = Problem.new()
problem.name = "BENE"
problem2 = Problem.new()
problem2.name = "BIANCA"

problems = [problem, problem2]



get '/update' do
	hashusers = {name: "foo"}
	problems = [problem]
	#redirect back
	redirect to("/bianca")
end

get '/:name' do
	erb :index, :locals => {:user => problem, :problems => problems}
end
