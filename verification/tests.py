"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[0, 1, 0, 3, 12]],
            "answer": [1, 3, 12, 0, 0]
        },
        {
            "input": [[0]],
            "answer": [0]
        }
    ],
    "Extra": [
        {
            "input": [[]],
            "answer": []
        },
        {
            "input": [[1, 2, 3, 4, 5, 6]],
            "answer": [1, 2, 3, 4, 5, 6]
        },
        {
            "input": [[0, 0, 0, 0, 0, 0, 0]],
            "answer": [0, 0, 0, 0, 0, 0, 0]
        },
        {
            "input": [[1, 2, 3, 0, 0, 0, 0]],
            "answer": [1, 2, 3, 0, 0, 0, 0]
        },
        {
            "input": [[0, 0, 0, 1, 2, 5, 6]],
            "answer": [1, 2, 5, 6, 0, 0, 0]
        }, 
        {
            "input": [[1, 0, 1, 0, 1, 0, 1]],
            "answer": [1, 1, 1, 1, 0, 0, 0]
        },
        {
            "input": [[-1, 0, 3, 0, -100, 0, 100]],
            "answer": [-1, 3, -100, 100, 0, 0, 0]
        }
    ]
}
