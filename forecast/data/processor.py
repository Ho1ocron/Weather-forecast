from csv import reader


async def get_citys_coords(name: str="Yekaterinburg", column_index = None) -> tuple[float]:
    with open("world_cities_data.csv", "r", newline="") as csvfile:
        csv_reader = reader(csvfile)
        found_lines = []
        for i, row in enumerate(csv_reader):
            if column_index is not None:
                if len(row) > column_index and name in row[column_index]:
                    found_lines.append((i, row))
            else:
                if any(name in cell for cell in row):
                    found_lines.append((i, row))
        lantitude, longitude = float(found_lines[0][1][2]), float(found_lines[0][1][3])
        return lantitude, longitude
    

if __name__ == "__main__":
    from asyncio import run
    print(run(get_citys_coords()))