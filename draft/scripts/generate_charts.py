#!/usr/bin/env python3
"""
Generate financial charts and visualizations for GIS Proposal
Author: GIS Startup Team
Date: February 2026
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
colors = ['#003366', '#0066cc', '#4c9900', '#808080']

# Create data directory if it doesn't exist
os.makedirs('../images', exist_ok=True)

# ============================================================================
# 1. Revenue Projection Chart
# ============================================================================

years = ['Year 1', 'Year 2', 'Year 3']
revenue = [30, 96.5, 204]
costs = [28, 47, 68]
profit = [2, 49.5, 136]

fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(years))
width = 0.25

bars1 = ax.bar(x - width, revenue, width, label='Revenue', color=colors[0])
bars2 = ax.bar(x, costs, width, label='Operating Costs', color=colors[3])
bars3 = ax.bar(x + width, profit, width, label='Net Profit', color=colors[2])

ax.set_ylabel('Amount (BDT Lakhs)', fontsize=12, fontweight='bold')
ax.set_title('3-Year Financial Projection', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}L',
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('../images/revenue_projection.png', dpi=300, bbox_inches='tight')
print("✓ Generated: revenue_projection.png")

# ============================================================================
# 2. Profit Margin Improvement
# ============================================================================

fig, ax = plt.subplots(figsize=(10, 6))

margins = [7, 51, 67]
ax.plot(years, margins, marker='o', linewidth=3, markersize=10, color=colors[1])
ax.fill_between(range(len(years)), margins, alpha=0.3, color=colors[1])

ax.set_ylabel('Profit Margin (%)', fontsize=12, fontweight='bold')
ax.set_title('Profit Margin Growth (Year 1-3)', fontsize=14, fontweight='bold')
ax.set_ylim(0, 100)
ax.grid(alpha=0.3)

# Add value labels
for i, (year, margin) in enumerate(zip(years, margins)):
    ax.text(i, margin + 2, f'{margin}%', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('../images/profit_margin.png', dpi=300, bbox_inches='tight')
print("✓ Generated: profit_margin.png")

# ============================================================================
# 3. Revenue Stream Composition (Year 3)
# ============================================================================

revenue_streams_y3 = {
    'Per-Project Services': 105,
    'Data Subscriptions': 30,
    'Custom Applications': 48,
    'Consulting & Training': 21
}

fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(
    revenue_streams_y3.values(),
    labels=revenue_streams_y3.keys(),
    autopct='%1.1f%%',
    colors=colors,
    startangle=90
)

ax.set_title('Year 3 Revenue Stream Composition (Total: BDT 204L)',
             fontsize=14, fontweight='bold')

# Make percentage text bold
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(11)

plt.tight_layout()
plt.savefig('../images/revenue_composition.png', dpi=300, bbox_inches='tight')
print("✓ Generated: revenue_composition.png")

# ============================================================================
# 4. Project Growth Trajectory
# ============================================================================

fig, ax = plt.subplots(figsize=(10, 6))

months = list(range(1, 37))
projects_cumulative = []

# Simulate project growth
for month in months:
    if month <= 12:
        # Year 1: 5-8 projects, average ~6
        cumulative = (month / 12) * 6
    elif month <= 24:
        # Year 2: 15-20 projects, add ~15 to existing 6
        cumulative = 6 + ((month - 12) / 12) * 15
    else:
        # Year 3: 40-50 projects, add ~45
        cumulative = 21 + ((month - 24) / 12) * 45

    projects_cumulative.append(cumulative)

ax.plot(months, projects_cumulative, linewidth=3, marker='o',
        markersize=3, color=colors[0], label='Cumulative Projects')

# Add phase markers
ax.axvline(x=3, color='gray', linestyle='--', alpha=0.5)
ax.axvline(x=12, color='gray', linestyle='--', alpha=0.5)
ax.axvline(x=24, color='gray', linestyle='--', alpha=0.5)

ax.text(1.5, 65, 'Phase 1:\nFoundation', ha='center', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
ax.text(7.5, 65, 'Phase 2:\nLaunch', ha='center', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
ax.text(18, 65, 'Phase 3:\nGrowth', ha='center', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
ax.text(30, 65, 'Phase 4:\nScaling', ha='center', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

ax.set_xlabel('Months', fontsize=12, fontweight='bold')
ax.set_ylabel('Cumulative Projects Completed', fontsize=12, fontweight='bold')
ax.set_title('Project Growth Trajectory (36 Months)', fontsize=14, fontweight='bold')
ax.grid(alpha=0.3)
ax.legend()

plt.tight_layout()
plt.savefig('../images/project_growth.png', dpi=300, bbox_inches='tight')
print("✓ Generated: project_growth.png")

# ============================================================================
# 5. Regional Revenue Contribution (Year 3)
# ============================================================================

regions = ['Dhaka\n(Central)', 'Chittagong\n(Southeast)', 'Khulna\n(Southwest)', 'Sylhet\n(Northeast)']
region_revenue = [50, 25, 35, 20]  # BDT Lakhs

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(regions, region_revenue, color=colors)

ax.set_ylabel('Revenue (BDT Lakhs)', fontsize=12, fontweight='bold')
ax.set_title('Year 3 Revenue by Region', fontsize=14, fontweight='bold')
ax.grid(axis='y', alpha=0.3)

# Add value labels
for bar, value in zip(bars, region_revenue):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
            f'BDT {value}L\n({value/sum(region_revenue)*100:.1f}%)',
            ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('../images/regional_revenue.png', dpi=300, bbox_inches='tight')
print("✓ Generated: regional_revenue.png")

# ============================================================================
# 6. Create Financial Data CSV
# ============================================================================

financial_data = pd.DataFrame({
    'Year': [1, 2, 3],
    'Revenue_BDT_L': [30, 96.5, 204],
    'Operating_Costs_BDT_L': [28, 47, 68],
    'Net_Profit_BDT_L': [2, 49.5, 136],
    'Profit_Margin_%': [7, 51, 67],
    'Projects_Completed': [6, 17, 45],
    'Area_Covered_SqKm': [13, 37, 75]
})

financial_data.to_csv('../data/financial_projections.csv', index=False)
print("✓ Generated: financial_projections.csv")

# ============================================================================
# 7. Create Market Data CSV
# ============================================================================

market_data = pd.DataFrame({
    'Region': ['Dhaka Central', 'Chittagong Southeast', 'Khulna Southwest', 'Sylhet Northeast'],
    'Hub_Launch_Month': [1, 3, 18, 30],
    'Target_Staff': [10, 4, 4, 3],
    'Year3_Revenue_BDT_L': [50, 25, 35, 20],
    'Primary_Sector': ['Government, Real Estate', 'Infrastructure, Tourism', 'Agriculture, NGOs', 'Research, Tea'],
    'Implementation_Status': ['Year 1', 'Year 1', 'Year 2', 'Year 3']
})

market_data.to_csv('../data/regional_strategy.csv', index=False)
print("✓ Generated: regional_strategy.csv")

# ============================================================================
# 8. Create Team Staffing Plan CSV
# ============================================================================

team_data = pd.DataFrame({
    'Role': [
        'Operations Manager',
        'GIS Analyst (Senior)',
        'Drone Pilot (Certified)',
        'Software Developer',
        'Data Processing Specialist',
        'Business Development',
        'Finance & Admin',
        'Part-time Consultants'
    ],
    'Year_1_Count': [1, 2, 2, 2, 2, 1, 1, 'Varies'],
    'Year_2_Count': [1, 4, 3, 3, 3, 1, 1, 'Varies'],
    'Year_3_Count': [1, 5, 3, 4, 4, 1, 1, 'Varies'],
    'Salary_Range_BDT': [
        '150-200K',
        '100-150K',
        '80-120K',
        '100-150K',
        '80-120K',
        '80-100K',
        '70-100K',
        'As needed'
    ]
})

team_data.to_csv('../data/team_structure.csv', index=False)
print("✓ Generated: team_structure.csv")

print("\n✅ All charts and data files generated successfully!")
print("\nGenerated files:")
print("  - images/revenue_projection.png")
print("  - images/profit_margin.png")
print("  - images/revenue_composition.png")
print("  - images/project_growth.png")
print("  - images/regional_revenue.png")
print("  - data/financial_projections.csv")
print("  - data/regional_strategy.csv")
print("  - data/team_structure.csv")
