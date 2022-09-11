def save_to_file(file_name,jobs):
    file = open(f"{file_name}.csv","w")
    file.write("Company,Position,URL\n")

    for job in jobs:
        file.write(f"{job['company']},{job['job']},{job['link']}\n")

    file.close()