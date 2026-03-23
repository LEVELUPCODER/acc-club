#!/usr/bin/env python3
# Fix the gallery section with proper HTML and different images

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the broken gallery section with proper HTML and different images
new_gallery = '''        <p class="text-slate-400 text-center mb-12 max-w-2xl mx-auto">
          Moments from our events, workshops, and team collaborations
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div class="gallery-item h-64 bg-slate-800 border border-slate-700 rounded-lg overflow-hidden relative" onclick="openModal(0)">
            <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?w=500&h=500&fit=crop" alt="Team Meeting" class="w-full h-full object-cover" />
            <div class="absolute inset-0 bg-black/40 opacity-0 hover:opacity-100 transition flex items-center justify-center"><i class="fas fa-search-plus text-white text-3xl"></i></div>
          </div>
          <div class="gallery-item h-64 bg-slate-800 border border-slate-700 rounded-lg overflow-hidden relative" onclick="openModal(1)">
            <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?w=500&h=500&fit=crop" alt="Data Workshop" class="w-full h-full object-cover" />
            <div class="absolute inset-0 bg-black/40 opacity-0 hover:opacity-100 transition flex items-center justify-center"><i class="fas fa-search-plus text-white text-3xl"></i></div>
          </div>
          <div class="gallery-item h-64 bg-slate-800 border border-slate-700 rounded-lg overflow-hidden relative" onclick="openModal(2)">
            <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=500&h=500&fit=crop" alt="Analysis Session" class="w-full h-full object-cover" />
            <div class="absolute inset-0 bg-black/40 opacity-0 hover:opacity-100 transition flex items-center justify-center"><i class="fas fa-search-plus text-white text-3xl"></i></div>
          </div>
          <div class="gallery-item h-64 bg-slate-800 border border-slate-700 rounded-lg overflow-hidden relative" onclick="openModal(3)">
            <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?w=500&h=500&fit=crop" alt="Presentation" class="w-full h-full object-cover" />
            <div class="absolute inset-0 bg-black/40 opacity-0 hover:opacity-100 transition flex items-center justify-center"><i class="fas fa-search-plus text-white text-3xl"></i></div>
          </div>
          <div class="gallery-item h-64 bg-slate-800 border border-slate-700 rounded-lg overflow-hidden relative" onclick="openModal(4)">
            <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?w=500&h=500&fit=crop" alt="Collaboration" class="w-full h-full object-cover" />
            <div class="absolute inset-0 bg-black/40 opacity-0 hover:opacity-100 transition flex items-center justify-center"><i class="fas fa-search-plus text-white text-3xl"></i></div>
          </div>
          <div class="gallery-item h-64 bg-slate-800 border border-slate-700 rounded-lg overflow-hidden relative" onclick="openModal(5)">
            <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?w=500&h=500&fit=crop" alt="Success" class="w-full h-full object-cover" />
            <div class="absolute inset-0 bg-black/40 opacity-0 hover:opacity-100 transition flex items-center justify-center"><i class="fas fa-search-plus text-white text-3xl"></i></div>
          </div>
        </div>'''

# Find and replace the broken section
import re
# Find from "Moments from our events" to the closing </div> after Success
pattern = r'<p class="text-slate-400 text-center mb-12 max-w-2xl mx-auto">\s*Moments from our events.*?</div>\s*</div>'
content = re.sub(pattern, new_gallery, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Gallery section fixed!")
