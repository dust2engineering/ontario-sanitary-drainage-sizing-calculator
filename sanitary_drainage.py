#!/usr/bin/env python3
"""Ontario sanitary drainage sizing (OBC Part 7): fixture units -> pipe sizes."""
import argparse, json, os
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "drainage-data.json")))

def smallest(table, load):
    for size, cap in table.items():
        if cap >= load: return size, cap
    return None, None

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--fu", type=float, required=True, help="total fixture units")
    p.add_argument("--fu-one-storey", type=float, default=0, help="largest fixture units drained from any one storey (stack check)")
    p.add_argument("--slope", default="1:100", choices=D["building_drain_table_7.4.10.6C_max_fu_by_slope"]["slopes"])
    a = p.parse_args()
    fu = a.fu
    bs, bc = smallest(D["branch_table_7.4.10.6B_max_fu"], fu)
    print(f"Total hydraulic load: {fu:g} fixture units")
    print(f"Branch (Table 7.4.10.6.-B): minimum NPS {bs} (capacity {bc} FU)" if bs else "Branch: exceeds NPS 12 table value")
    st = D["stack_table_7.4.10.6A_max_fu_total_and_per_storey"]
    pick = None
    for size, (tot, per) in st.items():
        if tot >= fu and (not a.fu_one_storey or per >= a.fu_one_storey): pick = (size, tot, per); break
    print(f"Stack (Table 7.4.10.6.-A): minimum NPS {pick[0]} (capacity {pick[1]} FU total, {pick[2]} FU from one storey)" if pick else "Stack: exceeds NPS 15 table value")
    idx = D["building_drain_table_7.4.10.6C_max_fu_by_slope"]["slopes"].index(a.slope)
    rows = D["building_drain_table_7.4.10.6C_max_fu_by_slope"]["rows"]
    pick = None
    for size, caps in rows.items():
        cap = caps[idx]
        if cap is not None and cap >= fu and float(size) >= 4: pick = (size, cap); break
    print(f"Building drain at slope {a.slope} (Table 7.4.10.6.-C): minimum NPS {pick[0]} (capacity {pick[1]} FU); building drains to a public sewer are never smaller than NPS 4" if pick else f"Building drain at slope {a.slope}: exceeds the table - increase slope or size beyond NPS 15")
    print("Preliminary only - verify against the OBC in force.")

if __name__ == "__main__":
    main()
