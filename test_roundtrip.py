import os
from fontTools.ttLib import TTFont

def test_and_print_results():
    """
    Tests IFT/IFTX table roundtrip for all .ttf fonts in the ./test_validation
    directory and prints a formatted markdown table of the results to the console.
    """
    test_dir = "./test_validation"
    
    # --- Check for test files ---
    try:
        all_files = sorted(os.listdir(test_dir))
        ttf_files = [f for f in all_files if f.endswith(".ttf")]
    except FileNotFoundError:
        print(f"Error: The directory '{test_dir}' was not found.")
        print("Please ensure the directory exists and contains your converted .ttf fonts.")
        return

    if not ttf_files:
        print(f"No .ttf files found in '{test_dir}'.")
        print("Please make sure you have converted the .woff2 files first.")
        return

    print(f"Found {len(ttf_files)} .ttf files. Starting tests...")

    # --- Run tests and collect results ---
    results_data = []
    for filename in ttf_files:
        print(f"  - Testing {filename}...")
        filepath = os.path.join(test_dir, filename)
        font = TTFont(filepath)

        # Default statuses
        ift_status = "Not present"
        iftx_status = "Not present"

        has_ift = "IFT " in font
        has_iftx = "IFTX" in font

        # Save and reload to check roundtrip if tables exist
        if has_ift or has_iftx:
            temp_path = os.path.join(test_dir, "temp.ttf")
            font.save(temp_path)
            rt_font = TTFont(temp_path)
            os.remove(temp_path)

            if has_ift:
                ift_table_orig = font["IFT "]
                ift_table_rt = rt_font["IFT "]
                if ift_table_orig.compile(font) == ift_table_rt.compile(rt_font):
                    ift_status = "Roundtrip successful"
                else:
                    ift_status = "Roundtrip FAILED"

            if has_iftx:
                iftx_table_orig = font["IFTX"]
                iftx_table_rt = rt_font["IFTX"]
                if iftx_table_orig.compile(font) == iftx_table_rt.compile(rt_font):
                    iftx_status = "Roundtrip successful"
                else:
                    iftx_status = "Roundtrip FAILED"
        
        results_data.append({
            "font": filename,
            "ift": ift_status,
            "iftx": iftx_status
        })

    # --- Format and print the results table ---
    print("\n--- Test Results ---")
    table = "| Font | IFT Status | IFTX Status |\n"
    table += "|---|---|---|\n"

    for result in results_data:
        table += f"| {result['font']} | {result['ift']} | {result['iftx']} |\n"

    print(table)


if __name__ == "__main__":
    test_and_print_results()
