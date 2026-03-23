"""
Testing utilities and test runner for ACC Club Backend API
"""

import sys
import json
from typing import Dict, Any

# Test data for API endpoints
TEST_DATA = {
    "registration": {
        "valid": {
            "email": "test@example.com",
            "name": "Test User",
            "enrollment_no": "2021001001",
            "department": "Computer Science",
            "semester": 4,
            "why_join": "Interested in analytics and consultancy",
            "phone": "9876543210"
        },
        "invalid_email": {
            "email": "invalid-email",
            "name": "Test User",
            "enrollment_no": "2021001001",
            "department": "Computer Science",
            "semester": 4,
            "why_join": "Test why join",
        },
        "invalid_semester": {
            "email": "test@example.com",
            "name": "Test User",
            "enrollment_no": "2021001001",
            "department": "Computer Science",
            "semester": 10,  # Invalid
            "why_join": "Test why join",
        }
    },
    "project": {
        "valid": {
            "name": "Test Project",
            "description": "This is a test project for testing purposes",
            "domain": "Finance",
            "status": "planning"
        },
        "invalid_name": {
            "name": "TP",  # Too short
            "description": "Test project",
            "domain": "Finance",
            "status": "planning"
        }
    },
    "team_member": {
        "valid": {
            "name": "John Doe",
            "position": "Team Lead",
            "domain": "Finance",
            "bio": "Experienced team lead",
            "email": "john@example.com",
            "phone": "9876543210"
        }
    }
}


class APITestCase:
    """Base class for API test cases"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.results = []
    
    def test_endpoint(self, method: str, endpoint: str, data: Dict = None, 
                     expected_status: int = 200) -> Dict[str, Any]:
        """Test an API endpoint"""
        url = f"{self.base_url}{endpoint}"
        
        import requests
        
        try:
            if method.upper() == "GET":
                response = requests.get(url, timeout=5)
            elif method.upper() == "POST":
                response = requests.post(url, json=data, timeout=5)
            elif method.upper() == "PUT":
                response = requests.put(url, json=data, timeout=5)
            elif method.upper() == "PATCH":
                response = requests.patch(url, json=data, timeout=5)
            elif method.upper() == "DELETE":
                response = requests.delete(url, timeout=5)
            else:
                raise ValueError(f"Unsupported method: {method}")
            
            passed = response.status_code == expected_status
            result = {
                "passed": passed,
                "method": method,
                "endpoint": endpoint,
                "status_code": response.status_code,
                "expected_status": expected_status,
                "response": response.json() if response.text else None
            }
            
            self.results.append(result)
            return result
            
        except requests.exceptions.ConnectionError:
            return {
                "passed": False,
                "error": "Connection failed - Is the server running?",
                "endpoint": endpoint
            }
        except Exception as e:
            return {
                "passed": False,
                "error": str(e),
                "endpoint": endpoint
            }
    
    def print_results(self):
        """Print test results"""
        print("\n" + "="*80)
        print("TEST RESULTS")
        print("="*80 + "\n")
        
        passed = sum(1 for r in self.results if r.get("passed"))
        total = len(self.results)
        
        for i, result in enumerate(self.results, 1):
            status = "✓ PASS" if result.get("passed") else "✗ FAIL"
            print(f"{i}. {status} | {result.get('method')} {result.get('endpoint')}")
            if not result.get("passed"):
                print(f"   Error: {result.get('error') or f'Expected {result.get(\"expected_status\")}, got {result.get(\"status_code\")}'}")
        
        print(f"\n{'='*80}")
        print(f"Total: {passed}/{total} passed")
        print("="*80 + "\n")
        
        return passed == total


def run_basic_tests():
    """Run basic API tests"""
    
    print("\n" + "="*80)
    print("STARTING API TESTS")
    print("="*80 + "\n")
    
    tester = APITestCase()
    
    # Test 1: Health check
    print("Test 1: Health check...")
    tester.test_endpoint("GET", "/health", expected_status=200)
    
    # Test 2: API info
    print("Test 2: API info...")
    tester.test_endpoint("GET", "/", expected_status=200)
    
    # Test 3: Create registration
    print("Test 3: Create registration...")
    tester.test_endpoint(
        "POST", "/api/registrations",
        data=TEST_DATA["registration"]["valid"],
        expected_status=201
    )
    
    # Test 4: List registrations
    print("Test 4: List registrations...")
    tester.test_endpoint("GET", "/api/registrations", expected_status=200)
    
    # Test 5: Get registration
    print("Test 5: Get registration (ID: 1)...")
    tester.test_endpoint("GET", "/api/registrations/1", expected_status=200)
    
    # Test 6: List team members
    print("Test 6: List team members...")
    tester.test_endpoint("GET", "/api/team", expected_status=200)
    
    # Test 7: Get team member
    print("Test 7: Get team member (ID: 1)...")
    tester.test_endpoint("GET", "/api/team/1", expected_status=200)
    
    # Test 8: List projects
    print("Test 8: List projects...")
    tester.test_endpoint("GET", "/api/projects", expected_status=200)
    
    # Test 9: Get project
    print("Test 9: Get project (ID: 1)...")
    tester.test_endpoint("GET", "/api/projects/1", expected_status=200)
    
    # Test 10: Create project
    print("Test 10: Create project...")
    tester.test_endpoint(
        "POST", "/api/projects",
        data=TEST_DATA["project"]["valid"],
        expected_status=201
    )
    
    # Print results
    all_passed = tester.print_results()
    
    return all_passed


def run_integration_tests():
    """Run integration tests (requires database)"""
    
    print("\n" + "="*80)
    print("INTEGRATION TESTS")
    print("="*80 + "\n")
    
    tester = APITestCase()
    
    # Create a registration
    print("Step 1: Create registration...")
    result = tester.test_endpoint(
        "POST", "/api/registrations",
        data=TEST_DATA["registration"]["valid"],
        expected_status=201
    )
    
    if not result.get("passed"):
        print("Cannot proceed with integration tests")
        return False
    
    reg_id = result.get("response", {}).get("data", {}).get("id")
    print(f"Created registration ID: {reg_id}")
    
    # Get the registration
    print("Step 2: Retrieve registration...")
    tester.test_endpoint("GET", f"/api/registrations/{reg_id}", expected_status=200)
    
    # Approve registration
    print("Step 3: Approve registration...")
    tester.test_endpoint(
        "PATCH", f"/api/registrations/{reg_id}/approve",
        expected_status=200
    )
    
    # Verify approval
    print("Step 4: Verify approval...")
    tester.test_endpoint("GET", f"/api/registrations/{reg_id}", expected_status=200)
    
    tester.print_results()
    return True


def run_performance_test():
    """Run performance tests"""
    
    import time
    import requests
    
    print("\n" + "="*80)
    print("PERFORMANCE TESTS")
    print("="*80 + "\n")
    
    base_url = "http://localhost:8000"
    
    # Test 1: List endpoint performance
    print("Test 1: GET /api/registrations performance...")
    start = time.time()
    for _ in range(10):
        requests.get(f"{base_url}/api/registrations")
    elapsed = time.time() - start
    avg_time = elapsed / 10
    print(f"  10 requests in {elapsed:.2f}s (avg: {avg_time*1000:.2f}ms)")
    
    # Test 2: Create endpoint performance
    print("Test 2: POST /api/registrations performance...")
    start = time.time()
    for i in range(5):
        requests.post(f"{base_url}/api/registrations", json={
            "email": f"perf{i}@example.com",
            "name": "Perf Test",
            "enrollment_no": f"2021{i:06d}",
            "department": "CS",
            "semester": 4,
            "why_join": "Performance test"
        })
    elapsed = time.time() - start
    avg_time = elapsed / 5
    print(f"  5 requests in {elapsed:.2f}s (avg: {avg_time*1000:.2f}ms)")
    
    print("\n" + "="*80)


def main():
    """Main test runner"""
    
    import argparse
    
    parser = argparse.ArgumentParser(description="ACC Club Backend API Tests")
    parser.add_argument("--basic", action="store_true", help="Run basic tests")
    parser.add_argument("--integration", action="store_true", help="Run integration tests")
    parser.add_argument("--performance", action="store_true", help="Run performance tests")
    parser.add_argument("--all", action="store_true", help="Run all tests")
    
    args = parser.parse_args()
    
    if args.all or not any([args.basic, args.integration, args.performance]):
        print("Running all tests...")
        run_basic_tests()
        run_integration_tests()
        run_performance_test()
    else:
        if args.basic:
            run_basic_tests()
        if args.integration:
            run_integration_tests()
        if args.performance:
            run_performance_test()


if __name__ == "__main__":
    main()
