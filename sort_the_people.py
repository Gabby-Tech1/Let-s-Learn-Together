class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        people = []

        for i in range(len(names)):
            people.append((names[i], heights[i]))
            
        for i in range(len(people)):
            max_index = i
            
            for j in range(i + 1, len(people)):
                if people[j][1] > people[max_index][1]:
                    max_index = j 
            people[i], people[max_index] = people[max_index], people[i]

        sorted_names = []

        for person in people:
            sorted_names.append(person[0])

        return sorted_names