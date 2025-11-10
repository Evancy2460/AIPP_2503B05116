import math
import json
import os
import sys
import argparse
from typing import Dict, Tuple, List


def debt_to_income_ratio(monthly_debt: float, monthly_income: float) -> float:
    if monthly_income <= 0:
        return 1.0
    return monthly_debt / monthly_income


LOANS_FILE = "loans.json"


def load_loans() -> List[Dict]:
    if not os.path.exists(LOANS_FILE):
        return []
    try:
        with open(LOANS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (OSError, json.JSONDecodeError):
        return []


def save_loans(loans: List[Dict]) -> None:
    try:
        with open(LOANS_FILE, "w", encoding="utf-8") as f:
            json.dump(loans, f, indent=2)
    except OSError as exc:
        print(f"Error saving loans: {exc}")


def next_loan_id(loans: List[Dict]) -> int:
    if not loans:
        return 1
    return max(int(l.get("id", 0)) for l in loans) + 1


def evaluate_applicant(app: Dict) -> Tuple[str, List[str]]:
    """
    Returns (decision, reasons).
    decision in {"APPROVE", "REVIEW", "REJECT"}.
    Simple transparent rules; gender/name fields are captured but not used in scoring.
    """
    reasons = []

    credit_score = float(app.get("credit_score", 0))
    annual_income = float(app.get("annual_income", 0))
    monthly_income = annual_income / 12.0
    loan_amount = float(app.get("loan_amount", 0))
    monthly_debt = float(app.get("monthly_debt", 0))
    tenure_years = float(app.get("tenure_years", 0))

    dti = debt_to_income_ratio(monthly_debt, monthly_income)
    income_multiple = loan_amount / max(1.0, annual_income)

    # Hard rejections
    if credit_score < 580:
        reasons.append("Credit score below 580 (hard reject).")
    if annual_income < 15000:
        reasons.append("Annual income below 15,000 (hard reject).")
    if tenure_years <= 0 or tenure_years > 30:
        reasons.append("Tenure must be between 1 and 30 years.")
    if dti > 0.6:
        reasons.append("Debt-to-income ratio above 60%.")
    if income_multiple > 8.0:
        reasons.append("Loan amount exceeds 8x annual income.")

    if reasons:
        return "REJECT", reasons

    # Soft checks for review band
    review_flags = []
    if credit_score < 650:
        review_flags.append("Credit score below 650 (manual review).")
    if dti > 0.4:
        review_flags.append("Debt-to-income ratio above 40% (manual review).")
    if loan_amount > 5.0 * annual_income:
        review_flags.append("Loan amount over 5x income (manual review).")
    if annual_income < 25000:
        review_flags.append("Annual income under 25,000 (manual review).")

    if review_flags:
        return "REVIEW", review_flags

    # Approve if clean
    return "APPROVE", ["Meets approval criteria."]


def format_currency(value: float) -> str:
    return f"₹{value:,.0f}"


def print_decision(app: Dict, decision: str, reasons: List[str]) -> None:
    print("\nDecision")
    print("--------")
    print(f"Name   : {app.get('name', '-')}\nGender : {app.get('gender', '-')}\n")
    print(f"Result : {decision}")
    for r in reasons:
        print(f" - {r}")


def demo_applicants() -> List[Dict]:
    return [
        {"name": "Aarav Sharma", "gender": "Male", "credit_score": 720, "annual_income": 900000, "monthly_debt": 10000, "loan_amount": 1200000, "tenure_years": 10},
        {"name": "Isha Patel", "gender": "Female", "credit_score": 610, "annual_income": 360000, "monthly_debt": 12000, "loan_amount": 1400000, "tenure_years": 15},
        {"name": "Rahul Verma", "gender": "Male", "credit_score": 560, "annual_income": 300000, "monthly_debt": 5000, "loan_amount": 400000, "tenure_years": 5},
        {"name": "Meera Nair", "gender": "Female", "credit_score": 680, "annual_income": 240000, "monthly_debt": 8000, "loan_amount": 1000000, "tenure_years": 20},
        {"name": "Alex Kim", "gender": "Non-binary", "credit_score": 700, "annual_income": 600000, "monthly_debt": 5000, "loan_amount": 1500000, "tenure_years": 25},
    ]


def run_demo():
    apps = demo_applicants()
    print("Loan Approval Demo (sample applicants)")
    print("--------------------------------------")
    for app in apps:
        decision, reasons = evaluate_applicant(app)
        print_decision(app, decision, reasons)
        print()


def prompt_float(label: str) -> float:
    while True:
        try:
            return float(input(label).strip())
        except ValueError:
            print("Please enter a valid number.")


def apply_loan() -> None:
    loans = load_loans()
    app: Dict = {}
    print("\nApply for a Loan")
    print("----------------")
    app["name"] = input("Name: ").strip()
    app["gender"] = input("Gender (Male/Female/Non-binary/Other): ").strip()
    app["credit_score"] = prompt_float("Credit score (300-850): ")
    app["annual_income"] = prompt_float("Annual income: ")
    app["monthly_debt"] = prompt_float("Current monthly debt payments: ")
    app["loan_amount"] = prompt_float("Requested loan amount: ")
    app["tenure_years"] = prompt_float("Tenure in years (1-30): ")

    decision, reasons = evaluate_applicant(app)

    loan_record = {
        "id": next_loan_id(loans),
        "applicant": {
            "name": app["name"],
            "gender": app["gender"],
        },
        "inputs": {
            "credit_score": app["credit_score"],
            "annual_income": app["annual_income"],
            "monthly_debt": app["monthly_debt"],
            "loan_amount": app["loan_amount"],
            "tenure_years": app["tenure_years"],
        },
        "decision": decision,
        "reasons": reasons,
    }
    loans.append(loan_record)
    save_loans(loans)

    print_decision(app, decision, reasons)
    print(f"Saved loan with ID: {loan_record['id']}")


def list_loans() -> None:
    loans = load_loans()
    if not loans:
        print("\nNo loans found.")
        return
    print(f"\nAll Loans ({len(loans)})")
    print("-----------------")
    for l in loans:
        name = l.get("applicant", {}).get("name", "-")
        gender = l.get("applicant", {}).get("gender", "-")
        decision = l.get("decision", "-")
        amount = l.get("inputs", {}).get("loan_amount", 0.0)
        print(f"ID {l.get('id')}: {name} ({gender}) | {format_currency(amount)} | {decision}")


def view_loan_details() -> None:
    loans = load_loans()
    if not loans:
        print("\nNo loans found.")
        return
    try:
        loan_id = int(input("Enter loan ID: ").strip())
    except ValueError:
        print("Please enter a valid ID number.")
        return
    match = next((l for l in loans if int(l.get("id", -1)) == loan_id), None)
    if not match:
        print("Loan not found.")
        return
    app = {
        "name": match.get("applicant", {}).get("name", "-"),
        "gender": match.get("applicant", {}).get("gender", "-"),
    }
    print_decision(
        {
            "name": app["name"],
            "gender": app["gender"],
        },
        match.get("decision", "-"),
        match.get("reasons", []),
    )
    inputs = match.get("inputs", {})
    print("\nDetails")
    print("-------")
    print(f"ID            : {match.get('id')}")
    print(f"Loan amount   : {format_currency(inputs.get('loan_amount', 0.0))}")
    print(f"Tenure years  : {inputs.get('tenure_years', 0)}")
    print(f"Credit score  : {inputs.get('credit_score', 0)}")
    print(f"Annual income : {format_currency(inputs.get('annual_income', 0.0))}")
    print(f"Monthly debt  : {format_currency(inputs.get('monthly_debt', 0.0))}")


def search_loans_by_name() -> None:
    loans = load_loans()
    if not loans:
        print("\nNo loans found.")
        return
    term = input("Enter name search term: ").strip().lower()
    results = [
        l for l in loans
        if term in str(l.get("applicant", {}).get("name", "")).lower()
    ]
    if not results:
        print("No matching loans.")
        return
    print(f"\nFound {len(results)} matching loans:")
    for l in results:
        name = l.get("applicant", {}).get("name", "-")
        gender = l.get("applicant", {}).get("gender", "-")
        decision = l.get("decision", "-")
        amount = l.get("inputs", {}).get("loan_amount", 0.0)
        print(f"ID {l.get('id')}: {name} ({gender}) | {format_currency(amount)} | {decision}")


def view_statistics() -> None:
    loans = load_loans()
    total = len(loans)
    print("\nStatistics")
    print("----------")
    print(f"Total loans: {total}")
    if total == 0:
        return

    by_decision: Dict[str, int] = {}
    by_gender: Dict[str, int] = {}
    total_amount = 0.0
    for l in loans:
        d = str(l.get("decision", "UNKNOWN"))
        by_decision[d] = by_decision.get(d, 0) + 1
        g = str(l.get("applicant", {}).get("gender", "Unknown"))
        by_gender[g] = by_gender.get(g, 0) + 1
        total_amount += float(l.get("inputs", {}).get("loan_amount", 0.0))

    print("\nBy decision:")
    for k, v in by_decision.items():
        pct = (v / total) * 100.0
        print(f" - {k}: {v} ({pct:.1f}%)")

    print("\nBy gender:")
    for k, v in by_gender.items():
        pct = (v / total) * 100.0
        print(f" - {k}: {v} ({pct:.1f}%)")

    avg_amount = total_amount / total if total else 0.0
    print(f"\nAverage loan amount: {format_currency(avg_amount)}")

def run_cli():
    print("Loan Approval System")
    print("--------------------")
    while True:
        print("\nMenu:")
        print("  1) Run demo on sample applicants")
        print("  2) Evaluate a custom applicant (no save)")
        print("  3) Apply for a loan (save)")
        print("  4) View all loans")
        print("  5) View loan details")
        print("  6) Search loans by name")
        print("  7) View statistics")
        print("  8) Exit")
        choice = input("Select an option (1-8): ").strip()
        if choice == "1":
            run_demo()
        elif choice == "2":
            app = {}
            app["name"] = input("Name: ").strip()
            app["gender"] = input("Gender (Male/Female/Non-binary/Other): ").strip()
            app["credit_score"] = prompt_float("Credit score (300-850): ")
            app["annual_income"] = prompt_float("Annual income: ")
            app["monthly_debt"] = prompt_float("Current monthly debt payments: ")
            app["loan_amount"] = prompt_float("Requested loan amount: ")
            app["tenure_years"] = prompt_float("Tenure in years (1-30): ")
            decision, reasons = evaluate_applicant(app)
            print_decision(app, decision, reasons)
        elif choice == "3":
            apply_loan()
        elif choice == "4":
            list_loans()
        elif choice == "5":
            view_loan_details()
        elif choice == "6":
            search_loans_by_name()
        elif choice == "7":
            view_statistics()
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1-8.")


def main():
    parser = argparse.ArgumentParser(description="Loan Approval System")
    sub = parser.add_subparsers(dest="cmd")

    # demo
    sub.add_parser("demo", help="Run demo on sample applicants (no save)")

    # evaluate (no save)
    p_eval = sub.add_parser("eval", help="Evaluate a custom applicant (no save)")
    p_eval.add_argument("--name", required=True)
    p_eval.add_argument("--gender", required=True, choices=["Male", "Female", "Non-binary", "Other"])
    p_eval.add_argument("--credit_score", required=True, type=float)
    p_eval.add_argument("--annual_income", required=True, type=float)
    p_eval.add_argument("--monthly_debt", required=True, type=float)
    p_eval.add_argument("--loan_amount", required=True, type=float)
    p_eval.add_argument("--tenure_years", required=True, type=float)

    # apply (save)
    p_apply = sub.add_parser("apply", help="Apply for a loan (save)")
    p_apply.add_argument("--name", required=True)
    p_apply.add_argument("--gender", required=True, choices=["Male", "Female", "Non-binary", "Other"])
    p_apply.add_argument("--credit_score", required=True, type=float)
    p_apply.add_argument("--annual_income", required=True, type=float)
    p_apply.add_argument("--monthly_debt", required=True, type=float)
    p_apply.add_argument("--loan_amount", required=True, type=float)
    p_apply.add_argument("--tenure_years", required=True, type=float)

    # list
    sub.add_parser("list", help="View all loans")

    # details
    p_details = sub.add_parser("details", help="View loan details by ID")
    p_details.add_argument("--id", required=True, type=int)

    # search
    p_search = sub.add_parser("search", help="Search loans by applicant name")
    p_search.add_argument("--name", required=True)

    # stats
    sub.add_parser("stats", help="View statistics")

    # seed demo loans (save demo_applicants to storage)
    sub.add_parser("seed", help="Seed storage with demo applicants as saved loans")

    args = parser.parse_args()

    if args.cmd == "demo":
        run_demo()
        return
    if args.cmd == "eval":
        app = {
            "name": args.name,
            "gender": args.gender,
            "credit_score": args.credit_score,
            "annual_income": args.annual_income,
            "monthly_debt": args.monthly_debt,
            "loan_amount": args.loan_amount,
            "tenure_years": args.tenure_years,
        }
        decision, reasons = evaluate_applicant(app)
        print_decision(app, decision, reasons)
        return
    if args.cmd == "apply":
        loans = load_loans()
        app = {
            "name": args.name,
            "gender": args.gender,
            "credit_score": args.credit_score,
            "annual_income": args.annual_income,
            "monthly_debt": args.monthly_debt,
            "loan_amount": args.loan_amount,
            "tenure_years": args.tenure_years,
        }
        decision, reasons = evaluate_applicant(app)
        loan_record = {
            "id": next_loan_id(loans),
            "applicant": {"name": app["name"], "gender": app["gender"]},
            "inputs": {
                "credit_score": app["credit_score"],
                "annual_income": app["annual_income"],
                "monthly_debt": app["monthly_debt"],
                "loan_amount": app["loan_amount"],
                "tenure_years": app["tenure_years"],
            },
            "decision": decision,
            "reasons": reasons,
        }
        loans.append(loan_record)
        save_loans(loans)
        print_decision(app, decision, reasons)
        print(f"Saved loan with ID: {loan_record['id']}")
        return
    if args.cmd == "list":
        list_loans()
        return
    if args.cmd == "details":
        loans = load_loans()
        match = next((l for l in loans if int(l.get("id", -1)) == args.id), None)
        if not match:
            print("Loan not found.")
            return
        app = {
            "name": match.get("applicant", {}).get("name", "-"),
            "gender": match.get("applicant", {}).get("gender", "-"),
        }
        print_decision(app, match.get("decision", "-"), match.get("reasons", []))
        inputs = match.get("inputs", {})
        print("\nDetails")
        print("-------")
        print(f"ID            : {match.get('id')}")
        print(f"Loan amount   : {format_currency(inputs.get('loan_amount', 0.0))}")
        print(f"Tenure years  : {inputs.get('tenure_years', 0)}")
        print(f"Credit score  : {inputs.get('credit_score', 0)}")
        print(f"Annual income : {format_currency(inputs.get('annual_income', 0.0))}")
        print(f"Monthly debt  : {format_currency(inputs.get('monthly_debt', 0.0))}")
        return
    if args.cmd == "search":
        term = args.name.strip().lower()
        loans = load_loans()
        results = [
            l for l in loans
            if term in str(l.get("applicant", {}).get("name", "")).lower()
        ]
        if not results:
            print("No matching loans.")
            return
        print(f"\nFound {len(results)} matching loans:")
        for l in results:
            name = l.get("applicant", {}).get("name", "-")
            gender = l.get("applicant", {}).get("gender", "-")
            decision = l.get("decision", "-")
            amount = l.get("inputs", {}).get("loan_amount", 0.0)
            print(f"ID {l.get('id')}: {name} ({gender}) | {format_currency(amount)} | {decision}")
        return
    if args.cmd == "stats":
        view_statistics()
        return
    if args.cmd == "seed":
        loans = load_loans()
        apps = demo_applicants()
        added = 0
        for app in apps:
            decision, reasons = evaluate_applicant(app)
            loan_record = {
                "id": next_loan_id(loans),
                "applicant": {"name": app["name"], "gender": app["gender"]},
                "inputs": {
                    "credit_score": app["credit_score"],
                    "annual_income": app["annual_income"],
                    "monthly_debt": app["monthly_debt"],
                    "loan_amount": app["loan_amount"],
                    "tenure_years": app["tenure_years"],
                },
                "decision": decision,
                "reasons": reasons,
            }
            loans.append(loan_record)
            added += 1
        save_loans(loans)
        print(f"Seeded {added} loans into {LOANS_FILE}.")
        return

    # Default: interactive menu
    run_cli()


if __name__ == "__main__":
    main()

