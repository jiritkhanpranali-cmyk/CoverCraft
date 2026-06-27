def recommend_best(results):

    if not results:

        return {
            "job": "No job found",
            "score": 0
        }


    return results[0]