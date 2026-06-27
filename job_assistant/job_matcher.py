def compare_jobs(resume_text, jobs):

    results = []


    resume_words = set(
        resume_text.lower().split()
    )


    for job_name, description in jobs.items():


        job_words = set(
            description.lower().split()
        )


        matched = resume_words.intersection(
            job_words
        )


        score = int(
            (len(matched) / max(len(job_words),1))
            *100
        )


        results.append(

            {
                "job": job_name,

                "score": score,

                "matched": list(matched)

            }

        )


    return sorted(

        results,

        key=lambda x:x["score"],

        reverse=True

    )