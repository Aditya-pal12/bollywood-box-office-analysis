import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import warnings
warnings.filterwarnings("ignore")

# =============================================
# DATA LOAD - APNI EXCEL FILE SE
# =============================================
df = pd.read_excel(r"C:\Users\palad\OneDrive\Documents\BOOL.xlsm", engine='openpyxl')

# =============================================
# OVERVIEW
# =============================================
print("=" * 50)
print("BOLLYWOOD DATASET OVERVIEW")
print("=" * 50)
print(f"Total Movies: {len(df)}")
print(f"Years Covered: {df['year'].min()} - {df['year'].max()}")
print(f"Hits: {(df['verdict']=='Hit').sum()} | Flops: {(df['verdict']=='Flop').sum()}")

print(f"\nTop 5 Highest Grossing Movies:")
print(df.nlargest(5, 'collection_cr')[['movie','collection_cr','verdict']].to_string(index=False))

print(f"\nTop Actors by Avg Collection (min 2 movies):")
actor_stats = df.groupby('lead_actor')['collection_cr'].agg(['mean','count'])
actor_stats = actor_stats[actor_stats['count'] >= 2].sort_values('mean', ascending=False).head(5)
print(actor_stats.round(1))

print(f"\nBest Genre by Avg Collection:")
print(df.groupby('genre')['collection_cr'].mean().sort_values(ascending=False).round(1))

# =============================================
# DASHBOARD
# =============================================
fig = plt.figure(figsize=(18, 14))
fig.patch.set_facecolor('#0D0D0D')
fig.suptitle("🎬 BOLLYWOOD BOX OFFICE ANALYSIS", fontsize=20,
             fontweight='bold', color='gold', y=0.98)

gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.55, wspace=0.4)

dark_bg = '#1A1A2E'
accent  = '#E94560'
gold    = '#FFD700'
text_color = 'white'

# --- Plot 1: Top 8 Movies ---
ax1 = fig.add_subplot(gs[0, :2])
ax1.set_facecolor(dark_bg)
top_movies = df.nlargest(8, 'collection_cr')
colors = [accent if v == 'Hit' else '#555' for v in top_movies['verdict']]
bars = ax1.barh(top_movies['movie'], top_movies['collection_cr'], color=colors, edgecolor='none')
ax1.set_title("Top 8 Movies by Box Office Collection", color=gold, fontweight='bold', pad=10)
ax1.set_xlabel("Collection (₹ Crores)", color=text_color)
ax1.tick_params(colors=text_color)
ax1.spines[['top','right','bottom','left']].set_color('#333')
for bar, val in zip(bars, top_movies['collection_cr']):
    ax1.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
             f'₹{val:.0f}Cr', va='center', color=gold, fontsize=8, fontweight='bold')
ax1.invert_yaxis()

# --- Plot 2: Hit vs Flop Pie ---
ax2 = fig.add_subplot(gs[0, 2])
ax2.set_facecolor(dark_bg)
verdict_counts = df['verdict'].value_counts()
wedges, texts, autotexts = ax2.pie(
    verdict_counts.values,
    labels=verdict_counts.index,
    autopct='%1.1f%%',
    colors=[accent, '#2ECC71'],
    startangle=90,
    textprops={'color': text_color, 'fontsize': 11}
)
for at in autotexts:
    at.set_color(gold)
    at.set_fontweight('bold')
ax2.set_title("Hit vs Flop Ratio", color=gold, fontweight='bold', pad=10)

# --- Plot 3: IMDb Rating vs Collection ---
ax3 = fig.add_subplot(gs[1, :2])
ax3.set_facecolor(dark_bg)
hits  = df[df['verdict'] == 'Hit']
flops = df[df['verdict'] == 'Flop']
ax3.scatter(flops['imdb_rating'], flops['collection_cr'], color='#555', alpha=0.7, s=60, label='Flop')
ax3.scatter(hits['imdb_rating'],  hits['collection_cr'],  color=accent,  alpha=0.9, s=80, label='Hit')
z = np.polyfit(df['imdb_rating'], df['collection_cr'], 1)
p = np.poly1d(z)
x_line = np.linspace(df['imdb_rating'].min(), df['imdb_rating'].max(), 100)
ax3.plot(x_line, p(x_line), color=gold, linewidth=2, linestyle='--', label='Trend')
ax3.set_title("IMDb Rating vs Box Office Collection", color=gold, fontweight='bold', pad=10)
ax3.set_xlabel("IMDb Rating", color=text_color)
ax3.set_ylabel("Collection (₹ Cr)", color=text_color)
ax3.tick_params(colors=text_color)
ax3.spines[['top','right','bottom','left']].set_color('#333')
ax3.legend(facecolor='#333', labelcolor=text_color)

# --- Plot 4: Genre Performance ---
ax4 = fig.add_subplot(gs[1, 2])
ax4.set_facecolor(dark_bg)
genre_avg = df.groupby('genre')['collection_cr'].mean().sort_values(ascending=True)
bars4 = ax4.barh(genre_avg.index, genre_avg.values, color='#16213E', edgecolor=accent, linewidth=1.5)
for bar, val in zip(bars4, genre_avg.values):
    bar.set_facecolor(accent if val == genre_avg.max() else '#16213E')
ax4.set_title("Avg Collection by Genre", color=gold, fontweight='bold', pad=10)
ax4.set_xlabel("Avg ₹ Crores", color=text_color)
ax4.tick_params(colors=text_color)
ax4.spines[['top','right','bottom','left']].set_color('#333')

# --- Plot 5: Yearly Trend ---
ax5 = fig.add_subplot(gs[2, :2])
ax5.set_facecolor(dark_bg)
yearly = df.groupby('year')['collection_cr'].sum().reset_index()
ax5.fill_between(yearly['year'], yearly['collection_cr'], alpha=0.3, color=accent)
ax5.plot(yearly['year'], yearly['collection_cr'], color=accent, linewidth=2.5, marker='o', markersize=5)
ax5.set_title("Yearly Box Office Collection Trend", color=gold, fontweight='bold', pad=10)
ax5.set_xlabel("Year", color=text_color)
ax5.set_ylabel("Total Collection (₹ Cr)", color=text_color)
ax5.tick_params(colors=text_color)
ax5.spines[['top','right','bottom','left']].set_color('#333')

# --- Plot 6: Top Directors ---
ax6 = fig.add_subplot(gs[2, 2])
ax6.set_facecolor(dark_bg)
dir_hits = df[df['verdict']=='Hit'].groupby('director').size().sort_values(ascending=True).tail(6)
ax6.barh(dir_hits.index, dir_hits.values, color=gold, edgecolor='none')
ax6.set_title("Directors with Most Hits", color=gold, fontweight='bold', pad=10)
ax6.set_xlabel("Number of Hits", color=text_color)
ax6.tick_params(colors=text_color)
ax6.spines[['top','right','bottom','left']].set_color('#333')

# =============================================
# SAVE DASHBOARD - SAME FOLDER MEIN
# =============================================
plt.savefig("bollywood_dashboard.png", dpi=150, bbox_inches='tight', facecolor='#0D0D0D')
print("\n✅ Dashboard saved as bollywood_dashboard.png")
plt.show()
