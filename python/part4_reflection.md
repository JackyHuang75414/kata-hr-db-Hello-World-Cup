# Part 4 — Reflection

Testing the same bug three times sounds like a waste of time at first. We found issues like negative zip codes and invalid dates during manual testing, wrote Playwright tests to prove them in the browser, then wrote integration tests to check the database directly. Same bug, three different tests. Why bother?

Turns out each layer tells us something different.

Manual testing is where everything starts. You mess around with the app, try weird inputs, and see what breaks. It's quick and creative, but you can't rerun it every time someone pushes code. Great for discovery, useless for regression.

Playwright tests show us what the user actually sees. You can't tell if a delete confirmation page is blank just by looking at the database — you need a browser to see the HTML. But these tests are slow and flaky. A selector changes, and suddenly everything breaks even though the app works fine.

Integration tests skip the browser entirely. An HTTP POST followed by a SQL query tells you exactly what's in the database. Fast, reliable, no flaky DOM. But if the UI breaks on special characters? Integration tests won't catch that.

We didn't have backend access, but if we did, unit tests would be the fourth layer — verifying that a function rejects bad input before it even touches the database. Fastest and most precise, but tells you nothing about the real user experience.

The point isn't that we tested the same thing three times. It's that each test answers a different question: Is there a bug? Does the user see it? Is the data wrong? Having all three means the bug has nowhere to hide.
