#!/usr/bin/env python3
files = ['index.html', 'awards.html', 'contact.html', 'studio.html']

for fname in files:
    with open(fname, 'r') as f:
        content = f.read()
    
    import re
    # Find the closing of the DOMContentLoaded handler
    pattern = r'(\s+});\n  },500\);\n\}\);\n</script>\n\n\n?<section id="studio">)'
    replacement = r'''    });
    // Auto-advance galleries like Instagram Stories
    galIds.forEach(function(id){
      (function(gid){
        var adv = setInterval(function(){
          var st=galState[gid];
          if(st&&st.items.length>1)slideGallery(gid,1);
        },4000);
        // Store ref for cleanup
        window['autoAdv_'+gid]=adv;
        var el=document.getElementById('main-'+gid);
        if(el){
          var ct=el.closest('.gallery-duo')||el.parentElement;
          ct.addEventListener('mouseenter',function(){clearInterval(window['autoAdv_'+gid])});
          ct.addEventListener('mouseleave',function(){window['autoAdv_'+gid]=setInterval(function(){slideGallery(gid,1)},4000)});
        }
      })(id);
    });
  },500);
});
</script>

<section id="studio">'''
    
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content, count=1)
        with open(fname, 'w') as f:
            f.write(content)
        print(f"{fname}: done")
    else:
        print(f"{fname}: pattern not found")

print("All done")
